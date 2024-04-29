<!-- eslint-disable -->
<template>
<div class="noncentral-item" v-if="!this.isCentral">
    <h3> {{this.title}} </h3>
</div>
<div class="central-item" v-if="this.isCentral">
        <slot></slot>
</div>
</template>

<script>
export default {
  name: "CarouselItem",
  props: {
    index: Number,
    title: String,
    isCentral: Boolean,
    maxHeight: String,
    itemWidth: String,
  },
  data() {
    return {
      centralHeight: this.maxHeight + "vh",
      centralWidth: this.itemWidth / 1.6 + "vw",
    };
  },
};
</script>

<style scoped>
.central-item,
.noncentral-item {
  margin: 0.5rem;
  border-radius: 35px;
  padding: 20px;
}

.central-item {
  height: v-bind(centralHeight);
  width: v-bind(centralWidth);
  background: rgba(255, 255, 255, 0.8);
  border: 1px solid rgba(125, 33, 103, 1);
  box-shadow: 2px 2px 2px 2px rgba(205, 204, 204, 0.4);

  overflow-y: scroll;
  overflow-x: hidden;
  align-content: center;
}

.noncentral-item {
  width: 300px;
  height: 150px;
  opacity: 0.6;

  background: rgba(125, 33, 103, 0.1);
  box-shadow: 2px 2px 2px 2px rgba(205, 204, 204, 0.4);
  position: relative;
}

.noncentral-item h3 {
  margin-top: 7vh;
  font-size: large;
}
</style>
