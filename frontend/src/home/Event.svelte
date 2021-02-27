<script>
    import SideNavbar from "@/components/SideNavbar.svelte"
    import Header from "@/components/Header.svelte"
    import ActionButton from "@/components/ActionButton.svelte"

    let date = " 26 Feb 2021"
</script>

<div class="wrapper">
    <SideNavbar/>
    <div class="content">
        <Header title="Tech Night #13" previousPath="/home"/>
        <div class="page-subheader">
			<p class="subheader-text">Created on {date}</p>
		</div>
        <div class="generated-content line">
            <div class="field-title">
                <p class="field-title-text">Generated Content</p>
                <ActionButton label="Copy" 
                    iconPath="/assets/icons/copy.svg" 
                    textColor="var(--dark-blue)"/>
            </div>
            <div class="content-writeup">
                *Tech Night #13 is here, back with streaming it live so you can watch it from the comfort of your own home!
“No money for Ecommerce Store...what to do? 🥺"
"How I wish there's a way to manage Telegram chat automatically... 🤔"
"I got my design...but how would it look like on the product? 🤨"
<br/>
<br/>
Tech Night Episode 13!
This coming Friday, sharing LIVE from Facebook... Shong Yang, Rain ,and Nunu will be introducing you to...
Free Ecommerce Storefront!
Telegram Chatbot!
Smartmockups in Canva!
<br/>
.
<br/>
❓ TECH NIGHT❓
Friends share new stuff with friends bi-weekly on a Friday Night! It’s fun! It’s safe! Anyone can participate! 😮
<br/>
.
<br/>
❓TECH NIGHT ❓
<br/>
1. Curious about the world of Tech?<br/>
2. Need a platform to share?<br/>
Let us know what's up at the end of the𝐜𝐡 𝐍𝐢𝐠𝐡𝐭 🤩<br/>
You’re probably also thinking?<br/>
This is not a SaaS kay? It’s FREE!!! Just let us know you're coming 👀<br/>
https://forms.gle/mQrnZeDDtkSVSNwA6<br/>
.<br/>
❓JOIN US Maybe ❓<br/>
⏰ 19.2.2021 6.00PM<br/>
📍 Facebook Live<br/>
            </div>
        </div>
        <div class="generated-poster line">
            <div class="field-title">
                <p class="field-title-text">Generated Poster</p>
                <ActionButton label="Download" 
                    iconPath="/assets/icons/download.svg" 
                    textColor="var(--dark-blue)"/>
            </div>
            <img src="/assets/example-poster.jpg" alt="" class="poster"/>
        </div>
    </div>
</div>

<style>
    .wrapper {
        width: 100%;
        display: flex;
    }
    .content {
        margin-top: 50px;
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
    }
    .page-subheader {
		display: flex;
		align-items: center;
		justify-content: space-between;
		border-bottom: 2px var(--light-grey) solid;
		margin-bottom: 20px;
        padding-bottom: 10px;
		width: 95%;
	}
	.subheader-text {
		font: var(--primary-font-regular);
		font-size: 10px;
        color: var(--dark-blue);
	}
    .field-title {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 10px;
    }
    .field-title-text {
        font: var(--primary-font-semibold)
    }
    .content-writeup {
        background-color: var(--light-grey);
        padding: 30px;
        width: 750px;
    }
    .poster {
        width: 750px;
    }
    .line {
        padding-bottom: 20px;
        border-bottom: 2px var(--light-grey) solid;
        margin-bottom: 30px;
    }
</style>