<script>
    import Card from "@/components/Card.svelte"
    import pushState from "@/utils/pushState";

    let data = {
        date: "26 Feb 2021",
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

    function nagivateEvent() {
        pushState("/home/event")
    }
</script>

<div class="card-wrapper" on:click={nagivateEvent}>
    <Card>
        <div class="wrapper">
            <div class="date">{data.date}</div>
            <div class="title">Tech Night #{data.episode}</div>

            {#each data.topic as topic}
                <div class="topic">- {topic.title}</div>
            {/each}
        </div>
    </Card>
</div>

<style>
    .card-wrapper {
        width: 250px;
        margin-right: 30px;
        margin-bottom: 20px;
        cursor: pointer;
    }
    .wrapper {
        padding: 20px;
    }
    .date {
        color: var(--dark-grey);
        font-size: 10px;
    }
    .title {
        color: var(--dark-blue);
        font: var(--primary-font-bold);
        font-size: 16px;
        margin-bottom: 20px;
    }
    .topic {
        color: var(--dark-blue);
        font: var(--primary-font-regular);
        font-size: 12px;
    }
</style>