<script>
	import Sidenav from "@/components/SideNavbar.svelte";

	import { fly, fade } from "svelte/transition";
	export let toggle = false;
	let navHeight, navSpacer;
	let windowWidth;
	let navbarCollapseInWidth = 850;
	$: {
		if (navSpacer) {
			navSpacer.style.setProperty("--height", `${navHeight}px`);
		} else if (navSpacer && windowWidth > navbarCollapseInWidth) {
			navSpacer.style.setProperty("--height", `0px`);
		}
	}
	function sidenavWrapperClicked(e) {
		if (e.target.classList.contains("sidenav")) {
			toggle = false;
		}
	}
</script>

<svelte:window bind:innerWidth={windowWidth} />
<div class="nav" bind:offsetHeight={navHeight}>
	<div class="nav__burger" on:click={() => (toggle = !toggle)}>
		<div class="burger__line" />
		<div class="burger__line" />
		<div class="burger__line" />
	</div>
	{#if !toggle}
		<div class="nav__logo" transition:fade={{ duration: 50 }}>
			<img src="/assets/stc-logo-word.svg" alt="stc logo" class="stc-icon" />
		</div>
	{/if}
</div>
<div class="nav_spacer" bind:this={navSpacer} />
{#if toggle}
	<div class="sidenav" on:click={sidenavWrapperClicked}>
		<div class="sidenav__inner" transition:fly={{ x: -150, duration: 100 }}>
			<Sidenav />
		</div>
	</div>
{/if}

<style>
	.nav {
		/* Layout */
		display: flex;
		align-items: center;
		padding: 15px;
		position: fixed;
		top: 0;
		left: 0;
		width: 100vw;
		z-index: 5;
		background-color: var(--white);
		/* Effect */
		box-shadow: 24px 4px 22px 13px rgba(0, 0, 0, 0.05);
	}
	.nav_spacer {
		height: var(--height);
	}
	.nav__burger {
		/* Layout */
		margin-right: 13px;
		/* Effect */
		cursor: pointer;
	}
	.burger__line {
		/* Layout */
		width: 20px;
		height: 3px;
		margin: 3px;
		/* Color */
		background-color: var(--purple-1);
	}
	.sidenav {
		width: 100vw;
		height: 100vh;
		position: absolute;
		z-index: 1;
		background-color: rgba(0, 0, 0, 0.4);
	}
</style>
