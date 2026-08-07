/**
 * form.js - Manages intake form validation, interaction, and data collection.
 */

import state from './state.js';
import { triggerAudit } from './api.js';

const ETSY_LISTING_URL_REGEX = /^https?:\/\/(www\.)?etsy\.com\/[a-zA-Z0-9-._~:\/?#[\]@!$&'()*+,;=]+/i;

/**
 * Validates Etsy listing URL format.
 * @param {string} url 
 * @returns {boolean}
 */
export function isValidEtsyUrl(url) {
  if (!url) return false;
  // A basic validation check to ensure it points to Etsy
  return ETSY_LISTING_URL_REGEX.test(url.trim());
}

/**
 * Binds form event handlers to the DOM elements.
 * @param {HTMLFormElement} formElement 
 */
export function initForm(formElement) {
  if (!formElement) return;

  const urlInput = formElement.querySelector('#audit-listing-url');
  const otherDetailsTextarea = formElement.querySelector('#audit-other-details');
  const statsRefInput = formElement.querySelector('#audit-stats-ref');
  const submitBtn = formElement.querySelector('#audit-submit-btn');

  formElement.addEventListener('submit', async (event) => {
    event.preventDefault();

    const listingUrl = urlInput.value.trim();
    if (!isValidEtsyUrl(listingUrl)) {
      state.set({
        status: 'error',
        error: 'Please enter a valid Etsy listing URL (e.g. https://www.etsy.com/listing/...)'
      });
      return;
    }

    // Collect checked differentiators
    const checkedBoxes = formElement.querySelectorAll('input[name="differentiators"]:checked');
    const sellerDifferentiators = Array.from(checkedBoxes).map(cb => cb.value);

    const payload = {
      listing_url: listingUrl,
      seller_differentiators: sellerDifferentiators,
      other_differentiator_details: otherDetailsTextarea.value.trim() || null,
      historical_stats_ref: statsRefInput.value.trim() || null
    };

    // Update state to loading
    state.set({ status: 'loading', error: null, report: null });

    try {
      const responseContext = await triggerAudit(payload);
      
      // The backend returns the full context, nested formatter_report holds output report.
      const report = responseContext.formatter_report || responseContext;

      state.set({
        status: 'success',
        report: report,
        error: null
      });
    } catch (err) {
      state.set({
        status: 'error',
        error: err.message || 'Audit execution failed. Please check the backend connection.'
      });
    }
  });

  // Track state changes to disable form fields during loading
  state.subscribe((currentState) => {
    const isLoading = currentState.status === 'loading';
    const isOffline = !currentState.backendOnline;

    const formInputs = formElement.querySelectorAll('input, textarea, button');
    formInputs.forEach(input => {
      if (isLoading) {
        input.disabled = true;
      } else {
        // Only keep disabled if backend is offline
        input.disabled = isOffline && input.id !== 'audit-listing-url' && input.id !== 'audit-stats-ref';
      }
    });

    if (submitBtn) {
      if (isLoading) {
        submitBtn.textContent = 'Analyzing listing...';
      } else {
        submitBtn.textContent = 'Run Audit';
      }
    }
  });
}
