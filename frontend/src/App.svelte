<script>
	import { onDestroy } from "svelte";
	import { fade } from "svelte/transition";
	import { quintOut } from "svelte/easing";
	import { Route, params } from "@/components/stores.js";
	import Navbar from "@/components/Navbar.svelte";
	import router from "@/rootRoutes";
	import Cookie from "js-cookie";
	import SideNavbar from "@/components/SideNavbar.svelte";
	import { disableNavbar } from "@/utils/store";

	let content;
	let uri = location.pathname;
	let windowWidth = 0;
	let navbarCollapseInWidth = 850;
	let toggle = false;
	let onPage = true;

	$: {
		if (windowWidth < navbarCollapseInWidth && !$disableNavbar) {
			document.body.style.setProperty("--main-display", "block");
			content && content.style.setProperty("--content-padding", "15px");
		} else {
			document.body.style.setProperty("--main-display", "flex");
			content && content.style.setProperty("--content-padding", "0px");
		}
	}

	if (uri != "/" && !Cookie.get("token")) window.location.href = "/";

	if (uri == "/" && Cookie.get("token")) window.location.href = "/home";

	function track(obj) {
		toggle = false;
		onPage = false;
		uri = obj.state || obj.uri || location.pathname;
		if (window.ga) ga.send("pageview", { dp: uri });
		setTimeout(() => {
			onPage = true;
		}, 130);
	}

	addEventListener("replacestate", track);
	addEventListener("pushstate", track);
	addEventListener("popstate", track);

	router.listen();

	onDestroy(router.unlisten);
</script>

<svelte:window bind:innerWidth={windowWidth} />
<main>
	{#if !$disableNavbar}
		{#if windowWidth < navbarCollapseInWidth}
			<Navbar bind:toggle />
		{:else}
			<SideNavbar />
		{/if}
	{/if}
	{#if onPage}
		<div
			class="content"
			bind:this={content}
			transition:fade={{ duration: 100, easing: quintOut }}
		>
			<svelte:component this={$Route} {$params} />
		</div>
	{/if}
</main>

<style>
	main {
		width: 100vw;
		display: var(--main-display);
	}
	.content {
		width: 100%;
		padding-left: var(--content-padding);
	}
</style>
