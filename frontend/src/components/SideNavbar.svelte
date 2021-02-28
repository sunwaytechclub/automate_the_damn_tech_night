<script>
    import AlertDialog from "@/components/AlertDialog.svelte"
    import Button from "@/components/Button.svelte";

    let pathName = location.pathname
    export let navs = [
        {
            iconPath: "/assets/icons/home-outline.svg",
            navTitle: "Home",
            navPath: "/home",
        },
        {
            iconPath: "/assets/icons/user.svg",
            navTitle: "Manage Speaker",
            navPath: "/speakers"
        },
        {
            iconPath: "/assets/icons/log-out.svg",
            navTitle: "Logout",
            navPath: "/logout"
        }
    ]

    let logoutDialog = false

    function logout() {
        logoutDialog = true;
    }
</script>

<div class="wrapper">
    <img src="/assets/stc-logo.svg" alt="stc logo" class="stc-icon"/>

    {#each navs as nav}
        {#if nav.navTitle == "Logout"}
            <div class="navigation {pathName.includes(nav.navPath) ? "active" : ""}" on:click={logout}>
                <img src={nav.iconPath} alt="" class="nav-icon"/>
                <p class="nav-title">{nav.navTitle}</p>
            </div>
        {:else}
            <a href={nav.navPath} class="navigation {pathName.includes(nav.navPath) ? "active" : ""}">
                <img src={nav.iconPath} alt="" class="nav-icon"/>
                <p class="nav-title">{nav.navTitle}</p>
            </a>
        {/if}
    {/each}
</div>

{#if logoutDialog}
    <AlertDialog bind:visible={logoutDialog}>
        <p class="logout-title">Are you sure?</p>
        <p class="logout-message">Are you sure want to logout?</p>
        <div class="logout-button-div">
            <Button secondaryButton on:click={() => logoutDialog=false} label="Cancel"/>
            <Button on:click label="Yes"/>
        </div>
    </AlertDialog>
{/if}

<style>
    .wrapper {
        width: 250px;
        height: 100vh;
        background: #FFFFFF;
        box-shadow: 4px 24px 22px 13px rgba(0, 0, 0, 0.05);
        margin-right: 100px;
        padding: 30px 40px;
    }
    .stc-icon {
        margin-bottom: 50px;
    }
    .navigation {
        display: flex;
        align-items: center;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
        cursor: pointer;
        width: 170px;
        text-decoration: none;
    }
    .active {
        background-color: var(--light-purple-2);
    }
    .nav-icon {
        margin-right: 10px;
    }
    .nav-title {
        font: var(--primary-font-bold);
        font-size: 12px;
        color: var(--purple-1);
    }
    .logout-title {
        font: var(--primary-font-bold);
        font-size: 24px;
        margin-bottom: 20px;
    }
    .logout-message {
        font: var(--primary-font-semibold);
        margin-bottom: 40px;
    }
    .logout-button-div {
        display: grid;
        grid-template-columns: auto auto;
        column-gap: 30px;
    }
</style>