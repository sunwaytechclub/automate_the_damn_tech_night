<script>
	import SideNavbar from "@/components/SideNavbar.svelte";
	import EventCard from "@/home/components/EventCard.svelte";
	import Header from "@/components/Header.svelte";
	import pushState from "@/utils/pushState.js";

	import Event from "@/services/event.js";
	import { onMount } from "svelte";

	onMount(async () => {
		let data = await Event.getAllEvents();
		events = data;
	});

	let events = [];

	function navigateCreateEvent() {
		pushState("/home/create-event/");
	}
</script>

<div class="wrapper">
	<div class="content">
		<Header title="Tech Night Event" />
		<div class="page-subheader">
			<p class="subheader-text">Manage Tech Night here!</p>
			<div class="create-button" on:click={navigateCreateEvent}>
				<img src="/assets/icons/plus-circle-outline.svg" alt="" />
				<p class="create-text">Create</p>
			</div>
		</div>
		<div class="events">
			{#each events as event}
				<EventCard data={event} />
			{/each}
		</div>
	</div>
</div>

<style>
	.wrapper {
		width: 100%;
		display: flex;
	}
	.content {
		margin-top: 20px;
		width: 70%;
	}
	.page-subheader {
		display: flex;
		align-items: center;
		justify-content: space-between;
		border-bottom: 2px var(--light-grey) solid;
		margin-bottom: 20px;
		width: 95%;
	}
	.subheader-text {
		font: var(--primary-font-regular);
		font-size: 14px;
	}
	.events {
		display: flex;
		flex-wrap: wrap;
	}
	.create-button {
		display: flex;
		align-items: center;
		padding: 10px;
		cursor: pointer;
	}
	.create-text {
		color: var(--purple-2);
		font: var(--primary-font-semibold);
		font-size: 14px;
		margin-left: 5px;
	}
</style>
