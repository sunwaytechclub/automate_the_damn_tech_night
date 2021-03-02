<script>
    import Card from "@/components/Card.svelte"
    import pushState from "@/utils/pushState";

    export let data = {
        datetime: "26 Feb 2021",
        episode: 3,
        topic: [
            {
                title: "Saleor"
            },
            {
                title: "React Native"
            }
        ]
    }

    let date = new Date(data.datetime);
    
    const options = {
        year: "numeric",
        month: "short",
        day: "numeric"
    };

    const formattedDate = date.toLocaleDateString("en", options)

    function nagivateEvent(id) {
        pushState(`/home/event/${id}`)
    }
</script>

<div class="card-wrapper" on:click={nagivateEvent(data.id)}>
    <Card>
        <div class="wrapper">
            <div class="date">{formattedDate}</div>
            <div class="title">Tech Night #{data.episode}</div>

            {#each data.topic as topic, i}
                {#if i < 2}
                    <div class="topic">- {topic.title}</div>
                {/if}
                {#if i >= 2}
                    <p class="dots">- ...</p>
                {/if}
            {/each}

        </div>
    </Card>
</div>

<style>
    .card-wrapper {
        width: 250px;
        height: 121px;
        margin-right: 30px;
        margin-bottom: 20px;
        cursor: pointer;
    }
    .wrapper {
        padding: 20px;
        height: 121px;
    }
    .date {
        font-size: 10px;
    }
    .title {
        color: var(--dark-blue);
        font: var(--primary-font-bold);
        font-size: 16px;
        margin-bottom: 10px;
    }
    .topic {
        color: var(--dark-blue);
        font: var(--primary-font-regular);
        font-size: 12px;
    }
    .dots {
        font: var(--primary-font-regular);
        font-size: 12px;
    }
    @media only screen and (max-width: 966px) {
		.card-wrapper {
            width: 300px;
        }
	}
</style>