<script>
    import TextInput from "@/components/TextInput.svelte"
    import Dropdown from "@/components/Dropdown.svelte"

    import { createEventDispatcher } from 'svelte';
    import { storeEventTopics, listTopics } from '@/components/stores.js';

    export let objAttributes = {};
    export let disabled = false;

    const dispatch = createEventDispatcher();

    let selectedValue

    let topicIndex = objAttributes.id - 1

    function handleSelect(event) {
        let value = event.detail.value
        $listTopics[topicIndex].selectedSpeaker = value
        $listTopics[topicIndex].title = objAttributes.titleInstance.value
        $listTopics[topicIndex].hook = objAttributes.hookInstance.value
        $listTopics[topicIndex].why = objAttributes.whyInstance.value
        $listTopics[topicIndex].what = objAttributes.whatInstance.value
    }

    function updateValue() {
        $listTopics[topicIndex].title = objAttributes.titleInstance.value
        $listTopics[topicIndex].hook = objAttributes.hookInstance.value
        $listTopics[topicIndex].why = objAttributes.whyInstance.value
        $listTopics[topicIndex].what = objAttributes.whatInstance.value
    }

    for (let i = 0; i < $storeEventTopics[topicIndex].speakers.length; i++) {
        if ($storeEventTopics[topicIndex].speaker == $storeEventTopics[topicIndex].speakers[i].value) {
            selectedValue =  $storeEventTopics[topicIndex].speakers[i]
            $listTopics[topicIndex].selectedSpeaker = $storeEventTopics[topicIndex].speakers[i].value
        }
    }

    function deleteTopic() {
		dispatch('delete', {
			topicIndex
		});
	}
        
</script>

<div class="speaker-header-div">
    <p class="speaker-header">Topic #{objAttributes.id}</p>
    {#if $storeEventTopics[topicIndex].deleteButton}
        <img src="/assets/icons/close-big.svg" alt="close" class="delete-topic-icon" on:click={deleteTopic}/>
    {:else}
    <div></div>
        {/if}
</div>
<div class="side-by-side">
    <TextInput value={$listTopics[topicIndex].title} label="Topic Title" placeholder="Topic Title" bind:instance={objAttributes.titleInstance} {disabled} on:keyup={updateValue}/>
    <Dropdown label="Speaker" placeholder="Speaker" 
        items={objAttributes.speakers} bind:selectedValue on:select={handleSelect} {disabled}/>
</div>
<div>
    <TextInput value={$listTopics[topicIndex].hook} label="Hook" placeholder="Hook" bind:instance={objAttributes.hookInstance} {disabled} on:keyup={updateValue}/>
    <TextInput value={$listTopics[topicIndex].why} label="Why" placeholder="Why?" bind:instance={objAttributes.whyInstance} {disabled} on:keyup={updateValue}/>
    <TextInput value={$listTopics[topicIndex].what} label="What" placeholder="What?!" bind:instance={objAttributes.whatInstance} {disabled} on:keyup={updateValue}/>
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
    .delete-topic-icon {
        position: absolute;
        right: 0;
        top: 0;
        cursor: pointer;
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
    .side-by-side {
        display: grid;
        grid-template-columns: auto auto;
        column-gap: 30px
    }
    @media only screen and (max-width: 966px) {
		.speaker-header:after {
            width: 60%;
        }
        .side-by-side {
            display: block
        }
	}
</style>