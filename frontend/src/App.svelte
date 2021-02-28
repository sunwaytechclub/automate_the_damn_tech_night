<script>
	import { onDestroy } from "svelte";
	import { Route, params } from "@/components/stores.js";
	import router from "@/rootRoutes";
	import Cookie from "js-cookie";

	let uri = location.pathname;

	if (uri != "/" && !Cookie.get('token')) window.location.href = "/"

	function track(obj) {
		uri = obj.state || obj.uri || location.pathname;
		if (window.ga) ga.send("pageview", { dp: uri });
	}

	addEventListener("replacestate", track);
	addEventListener("pushstate", track);
	addEventListener("popstate", track);

	router.listen();

	onDestroy(router.unlisten);
</script>

<main>
	<svelte:component this={$Route} {$params} />
</main>
