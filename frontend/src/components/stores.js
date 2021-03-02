import { writable } from 'svelte/store';

// Stores for router
export const Route = writable(undefined);
export const params = writable(undefined);

export let storeEvent = writable({});
export let storeSpeaker = writable({});
export let idIncrement = writable({});
export let selectedSpeakers = writable([])
export let storeSpeakerPositions = writable([])
export let listPositions = writable([])
export let storeEventTopics = writable([])
export let listTopics = writable([])

export let alert = writable({})