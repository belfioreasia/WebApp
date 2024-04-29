<!-- eslint-disable -->
<template>
    <div class="summary-band">
        <div class="summary-container" v-for="(title, index) in this.titles">
            <div class="summary-item">
                <img v-if="this.icons[index]!='null'" :src="require(`@/icons/${image[index]}`)"> 
                <div class="text-area">
                    <h3> {{title}} </h3>
                    <p> {{this.bodies[index]}} </p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
/* eslint-disable */
export default {
    name: "SummaryBand",
    data() {
        return {
            band_width: this.width + "vw",
            band_height: this.height + "vh",
            image: this.icons,
            img_width: (parseInt(this.width)/3.5) + "vw",
            border_color:  this.color,
        }
    },
    props: {
        icons: Array,
        titles: Array,
        bodies: Array,
        width: String,
        height: String,
        color: String,
    },
};
</script>

<style scoped>
.summary-band {
    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
    align-items: left;
    gap: 2em;
    text-align: left;
    margin: 1rem 0.2rem 0rem 0.2rem;
    padding: 0.1rem;
}

.summary-container {
    display: flex;
    place-items: center;
    place-content: flex-start;
    border-radius: 15px;
    width: v-bind(band_width);
    height: v-bind(band_height);
    border: 1px solid v-bind(border_color);
    box-shadow: 2px 2px 2px 2px rgba(205, 204, 204, 0.2);
    min-width: 180px;
    transition: transform 200ms ease-in-out;
}

.summary-container:hover {
    transform: scale(1.05);
    box-shadow: 2px 2px 2px 2px rgba(205, 204, 204, 0.5);
}

.summary-item {
    display: flex;
    flex-direction: row;
    place-items: center;
    gap: 5px;
    margin-inline-start: 0.5vw;
}


img {
    width: v-bind(img_width);
    max-width:  55px;
}

.text-area {
    display: flex;
    flex-direction: column;
    align-items: left;
}

p {
    margin: 0px;
    font-size: small;
}

h3 {
    margin: 0px;
    font-size: medium;
    color: v-bind(border_color);
}

.body {
    color: rgb(72, 71, 73);
}
</style>
