import { writable } from 'svelte/store';

// Stores for router
export const Route = writable(undefined);
export const params = writable(undefined);

export let storeFE = writable({});
export let idIncrement = writable({});
export let selectedSpeakers = writable([])