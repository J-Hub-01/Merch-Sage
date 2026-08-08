/**
 * api.js - Client wrapper for contacting the MerchSage FastAPI backend.
 */

const DEFAULT_BASE_URL = 'https://merch-sage.onrender.com';

export function getBaseUrl() {
  // If served locally on port 8000 or same-origin backend, use current origin, otherwise fallback to local backend.
  if (window.location.origin && window.location.origin.includes(':8000')) {
    return window.location.origin;
  }
  return DEFAULT_BASE_URL;
}

/**
 * Checks connectivity with the backend server.
 * @returns {Promise<boolean>} Resolves to true if the backend health check passes.
 */
export async function checkBackendHealth() {
  const baseUrl = getBaseUrl();
  try {
    const response = await fetch(`${baseUrl}/health`, {
      method: 'GET',
      headers: { 'Accept': 'application/json' }
    });
    if (!response.ok) return false;
    const data = await response.json();
    return data && data.status === 'ok';
  } catch (error) {
    console.warn('Backend health check failed:', error);
    return false;
  }
}

/**
 * Triggers the Discoverability audit pipeline.
 * @param {Object} payload 
 * @param {string} payload.listing_url
 * @param {string[]} payload.seller_differentiators
 * @param {string} [payload.other_differentiator_details]
 * @param {string} [payload.historical_stats_ref]
 * @returns {Promise<Object>} The full audit response context.
 */
export async function triggerAudit(payload) {
  const baseUrl = getBaseUrl();
  const response = await fetch(`${baseUrl}/api/audit`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    },
    body: JSON.stringify(payload)
  });

  if (!response.ok) {
    let errorDetail = 'Audit request failed';
    try {
      const errorJson = await response.json();
      if (errorJson && errorJson.detail) {
        errorDetail = typeof errorJson.detail === 'string'
          ? errorJson.detail
          : JSON.stringify(errorJson.detail);
      }
    } catch (_) { }
    throw new Error(errorDetail);
  }

  return await response.json();
}
