<script>
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
</script>

<div class="wrapper">
    <img src="/assets/stc-logo.svg" alt="stc logo" class="stc-icon"/>

    {#each navs as nav}
        <div class="navigation {pathName.includes(nav.navPath) ? "active" : ""}">
            <img src={nav.iconPath} alt="" class="nav-icon"/>
            <p class="nav-title">{nav.navTitle}</p>
        </div>
    {/each}
</div>

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
</style>