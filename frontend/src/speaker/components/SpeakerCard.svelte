<script>
    import Card from "@/components/Card.svelte"
    import pushState from "@/utils/pushState";

    let speaker = {
        name: "Rain Chai Chang Cheng Cheng",
        position: "STC Head of MarketingSTC Head of Marketing"
    }

    function nagivateEvent() {
        pushState("/speakers/speaker")
    }
</script>

<div class="card-wrapper" on:click={nagivateEvent}>
    <Card>
        <div class="wrapper">
            <img src="/assets/example-avatar.png" alt="" class="avatar"/>
            <div>
                <p class="speaker-name">{speaker.name}</p>
                <p class="speaker-position">{speaker.position}</p>
            </div>
            <img src="/assets/icons/edit.svg" alt="" class="edit-icon"/>
        </div>
    </Card>
</div>

<style>
    .card-wrapper {
        width: 300px;
        margin-right: 30px;
        margin-bottom: 20px;
        cursor: pointer;
    }
    .wrapper {
        padding: 20px;
        display: flex;
        align-items: center;
        position: relative;
    }
    .avatar {
        width: 64px;
        border-radius: 50%;
        margin-right: 20px;
    }
    .speaker-name {
        font: var(--primary-font-bold);
        font-size: 14px;
        max-width: 170px;
    }
    .speaker-position {
        color: var(--dark-grey);
        font-size: 12px;
    }
    .edit-icon {
        position: absolute;
        right: 20px;
        top: 20px;
        width: 18px;
    }
</style>