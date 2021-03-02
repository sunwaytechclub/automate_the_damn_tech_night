<script>
    import TextInput from "@/components/TextInput.svelte"
    
    import { createEventDispatcher } from 'svelte';
    import { listPositions, storeSpeakerPositions } from '@/components/stores.js';

    export let objAttributes = {};
    export let disabled = false;

    const dispatch = createEventDispatcher();

    let positionIndex = objAttributes.id - 1

    function updateValue() {
        $listPositions[positionIndex] = objAttributes.position.value
    }

    function deletePosition() {
		dispatch('delete', {
			positionIndex
		});
	}
</script>

<div class="speaker-header-div">
    <p class="speaker-header">Position #{objAttributes.id}</p>
    {#if $storeSpeakerPositions[positionIndex].deleteButton}
        <img src="/assets/icons/close-big.svg" alt="close" class="delete-position-icon" on:click={deletePosition}/>
    {:else}
    <div></div>
        {/if}
</div>
<div>
    <TextInput value={$listPositions[positionIndex]} label="Position" placeholder="Position" bind:instance={objAttributes.position} {disabled} on:keyup={updateValue}/>
</div>

<style>
    .speaker-header-div {
        position: relative;
        margin-bottom: 15px;
        margin-top: 20px;
    }
    .speaker-header {
        font: var(--primary-font-bold);
    }
    .speaker-header:after {
        position: absolute;
        top: 51%;
        left: 100px;
        overflow: hidden;
        width: 80%;
        height: 2px;
        content: '\a0';
        background-color: var(--light-grey)
    }
    .delete-position-icon {
        position: absolute;
        right: 0;
        top: 0;
        cursor: pointer;
    }
    @media only screen and (max-width: 966px) {
		.speaker-header:after {
            width: 60%;
        }
	}
</style>