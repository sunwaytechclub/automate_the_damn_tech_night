import run from "@/utils/run";
import Router from "@/utils/generateRouter";

let ROUTES = [
    // Current routes go here
    ['/', run(import("./Index.svelte"))],
    ['/speaker/:id', run(import("./EditSpeaker.svelte"))],
    ['/create-speaker', run(import("./CreateSpeaker.svelte"))],
]
export default Router(ROUTES)