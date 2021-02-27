import run from "@/utils/run";
import Router from "@/utils/generateRouter";

let ROUTES = [
    // Current routes go here
    ['/', run(import("./Index.svelte"))],
    ['/create-event', run(import("./CreateEvent.svelte"))],
    ['/event', run(import("./Event.svelte"))],
]
export default Router(ROUTES)