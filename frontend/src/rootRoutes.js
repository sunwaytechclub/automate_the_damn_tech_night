/*
 Global router, see routes.sample.js if you would like to create new routes in folder.
*/
import Navaid from "navaid";
import HomeRouter from "@/home/routes";
import AuthRouter from "@/auth/routes";
import FormRouter from "@/form/routes";
import SpeakerRouter from "@/speaker/routes";
import run from "@/utils/run";

const router = Navaid("/", run(import("./404.svelte")));

// Add first-level child routers here
[...HomeRouter("home")].map((route) => {
	router.on(route[0], route[1]);
});

[...AuthRouter("")].map((route) => {
	router.on(route[0], route[1]);
});

[...FormRouter("form")].map((route) => {
	router.on(route[0], route[1]);
});

[...SpeakerRouter("speakers")].map((route) => {
	router.on(route[0], route[1]);
});

export default router;
