/**
 * renderer.js - Renders UI state changes, errors, loading indicators, and report results.
 */

import state from './state.js';

export function initRenderer() {
  const errorPanel = document.querySelector('#audit-error');
  const resultsPanel = document.querySelector('#audit-results');
  const spinnerContainer = document.querySelector('#audit-spinner');

  state.subscribe((currentState) => {
    // 1. Handle Loading States
    if (currentState.status === 'loading') {
      if (spinnerContainer) spinnerContainer.style.display = 'flex';
      if (errorPanel) errorPanel.style.display = 'none';
      if (resultsPanel) resultsPanel.style.display = 'none';
    } 
    // 2. Handle Error States
    else if (currentState.status === 'error') {
      if (spinnerContainer) spinnerContainer.style.display = 'none';
      if (resultsPanel) resultsPanel.style.display = 'none';
      
      if (errorPanel) {
        errorPanel.querySelector('.error-message').textContent = currentState.error || 'Unknown error occurred.';
        errorPanel.style.display = 'block';
        errorPanel.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
    } 
    // 3. Handle Success / Result Rendering
    else if (currentState.status === 'success' && currentState.report) {
      if (spinnerContainer) spinnerContainer.style.display = 'none';
      if (errorPanel) errorPanel.style.display = 'none';
      
      if (resultsPanel) {
        renderAuditReport(resultsPanel, currentState.report);
        resultsPanel.style.display = 'block';
        resultsPanel.scrollIntoView({ behavior: 'smooth' });
      }
    } 
    // 4. Idle State
    else {
      if (spinnerContainer) spinnerContainer.style.display = 'none';
      if (errorPanel) errorPanel.style.display = 'none';
      if (resultsPanel) resultsPanel.style.display = 'none';
    }
  });
}

/**
 * Updates the DOM of the results panel with data from the audit report.
 * @param {HTMLElement} panel 
 * @param {Object} report 
 */
function renderAuditReport(panel, report) {
  // Extract info safely
  const diagnosedBranch = report.diagnosed_branch || 'N/A';
  const classification = report.classification || 'N/A';
  const auditId = report.audit_id || 'N/A';
  
  // Set meta info
  panel.querySelector('#meta-branch').textContent = diagnosedBranch;
  panel.querySelector('#meta-category').textContent = classification;
  panel.querySelector('#meta-id').textContent = auditId;

  // Retrieve proposed solutions (if any)
  const proposedSolutions = report.proposed_solutions || [];
  const primarySolution = proposedSolutions[0]?.solution || {};
  const proposedTitle = primarySolution.proposed_title || 'No title generated';
  const proposedTags = primarySolution.proposed_tags || [];
  const justification = primarySolution.justification || 'No justification provided';
  const claims = primarySolution.claims_made || [];

  // Title render
  panel.querySelector('#result-title').textContent = proposedTitle;

  // Tags render (clear old ones and insert new pills)
  const tagsContainer = panel.querySelector('#result-tags');
  if (tagsContainer) {
    tagsContainer.innerHTML = '';
    proposedTags.forEach(tag => {
      const pill = document.createElement('span');
      pill.className = 'tag-pill';
      pill.textContent = tag;
      tagsContainer.appendChild(pill);
    });
  }

  // Justification render
  panel.querySelector('#result-justification').textContent = justification;

  // Verification results badges & details
  const verification = report.verification_results || {};
  const business = report.business_verification || {};

  // Render Structural Verification Status
  const structPassed = verification.structural?.passed ?? false;
  const structBadge = panel.querySelector('#badge-structural');
  if (structBadge) {
    structBadge.className = `verification-badge ${structPassed ? 'badge-pass' : 'badge-fail'}`;
    structBadge.innerHTML = structPassed ? 'Structural Valid ✓' : 'Structural Failed ✗';
  }

  // Render Factual/Legal Verification Status
  const factualPassed = verification.factual_legal?.passed ?? false;
  const factualBadge = panel.querySelector('#badge-factual');
  if (factualBadge) {
    factualBadge.className = `verification-badge ${factualPassed ? 'badge-pass' : 'badge-fail'}`;
    factualBadge.innerHTML = factualPassed ? 'Factual Compliance ✓' : 'Factual Conflict ✗';
  }

  // Render Business Compatibility Status
  const bizPassed = business.is_compatible ?? false;
  const bizBadge = panel.querySelector('#badge-business');
  if (bizBadge) {
    bizBadge.className = `verification-badge ${bizPassed ? 'badge-pass' : 'badge-fail'}`;
    bizBadge.innerHTML = bizPassed ? 'Business Alignment ✓' : 'Business Conflict ✗';
  }

  // Render claims check list (if any)
  const claimsContainer = panel.querySelector('#claims-list');
  if (claimsContainer) {
    claimsContainer.innerHTML = '';
    if (claims.length > 0) {
      claims.forEach(claim => {
        const item = document.createElement('li');
        item.className = 'claim-item';
        item.innerHTML = `<span class="check-icon">✓</span> ${claim}`;
        claimsContainer.appendChild(item);
      });
    } else {
      claimsContainer.innerHTML = '<li class="claim-item empty">No custom claims verified</li>';
    }
  }

  // Update total evidence counter
  const evidenceCount = report.total_evidence_objects || 0;
  panel.querySelector('#evidence-count').textContent = evidenceCount;
}
