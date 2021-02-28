<script>
    import SideNavbar from "@/components/SideNavbar.svelte"
    import ActionButton from "@/components/ActionButton.svelte"
	import SpeakerCard from "@/speaker/components/SpeakerCard.svelte"
	import Header from "@/components/Header.svelte"
	import pushState from "@/utils/pushState.js"

	import Speaker from "@/services/speaker.js"
	import { onMount } from "svelte";

	let speakers = []

	onMount(async () => {
		
		let response = await Speaker.getAllSpeakers()
		speakers = response
		console.log(speakers)
	})

	// $: allSpeakers = speakers

	function navigateCreateEvent() {
		pushState("/speakers/create-speaker")
	}

</script>

<div class="wrapper">
    <SideNavbar/>
    <div class="content">
        <Header title="Manage speakers"/>
		<div class="page-subheader">
			<p class="subheader-text">Manage spekers here!</p>
			<ActionButton label="Create Speaker" 
                    iconPath="/assets/icons/user-plus.svg" 
                    textColor="var(--purple-2)" on:click={navigateCreateEvent}/>
		</div>
		<div class="events">
			{#await speakers}
				<!-- TODO: loader -->
			{:then}
				{#each speakers as speaker}
					<SpeakerCard speaker={speaker}/>
				{/each}
			{/await}
		</div>
    </div>
</div>

<style>
    .wrapper {
        width: 100%;
        display: flex;
    }
    .content {
        margin-top: 40px;
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
		flex-wrap: wrap
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