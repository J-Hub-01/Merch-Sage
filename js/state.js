/**
 * state.js - Simple state manager for the MerchSage frontend application.
 */

class AppState {
  constructor() {
    this._state = {
      status: 'idle', // 'idle' | 'loading' | 'success' | 'error'
      error: null,
      report: null,
      backendOnline: true
    };
    this._listeners = new Set();
  }

  /**
   * Returns a copy of the current state.
   */
  get() {
    return { ...this._state };
  }

  /**
   * Updates state properties and triggers subscribers.
   * @param {Object} updates 
   */
  set(updates) {
    const prevState = { ...this._state };
    this._state = { ...this._state, ...updates };

    // Check if anything actually changed
    const changed = Object.keys(updates).some(key => prevState[key] !== this._state[key]);
    if (changed) {
      this._notify();
    }
  }

  /**
   * Subscribes a listener function to state changes.
   * @param {Function} listener 
   * @returns {Function} Unsubscribe function
   */
  subscribe(listener) {
    this._listeners.add(listener);
    // Call immediately to establish baseline
    listener(this._state);
    return () => this._listeners.delete(listener);
  }

  _notify() {
    for (const listener of this._listeners) {
      try {
        listener(this._state);
      } catch (err) {
        console.error('Error in state subscriber:', err);
      }
    }
  }
}

export const state = new AppState();
export default state;
