import run from "@/utils/run";
import Router from "@/utils/generateRouter";

let ROUTES = [
    // Current routes go here
    ['/', run(import("./Index.svelte"))],
    ['/create-event', run(import("./CreateEvent.svelte"))],
    ['/event/:id', run(import("./Event.svelte"))],
    ['/event/edit/:id', run(import("./EditEvent.svelte"))],
]
export default Router(ROUTES)