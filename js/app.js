/**
 * app.js - Main entry point bootstrapping the MerchSage modular frontend.
 */

import state from './state.js';
import { checkBackendHealth } from './api.js';
import { initForm } from './form.js';
import { initRenderer } from './renderer.js';

document.addEventListener('DOMContentLoaded', async () => {
  console.log('Initializing MerchSage Frontend Client...');

  // Initialize UI renderer
  initRenderer();

  // Initialize form handler
  const formElement = document.querySelector('#audit-form-element');
  if (formElement) {
    initForm(formElement);
  } else {
    console.error('Audit form element (#audit-form-element) not found on page.');
  }

  // Pre-flight health check to verify backend connectivity
  const isOnline = await checkBackendHealth();
  state.set({ backendOnline: isOnline });

  if (!isOnline) {
    console.warn('Backend server appears offline or unreachable.');
    // Set a friendly warning on page
    state.set({
      status: 'error',
      error: 'FastAPI Backend unreachable. Please start the backend service (uvicorn backend.main:app --reload) to run real audits.'
    });
  }
});
