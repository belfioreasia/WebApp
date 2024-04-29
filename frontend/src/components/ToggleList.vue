<!-- eslint-disable -->
<template>
        <div @click="expandSection" v-if="this.isExpanded" class="expanded">
            <h3> {{title}} </h3>
            <slot></slot>
        </div>
        <div @click="expandSection" v-if="!this.isExpanded" class="collapsed">
            <h3> {{title}} </h3>
        </div>
</template>

<script>
export default {
  name: "ToggleList",
  data() {
    return {
      isExpanded: false,
      itemWidth: this.width + "vw",
    };
  },
  props: {
    title: String,
    index: Number,
    width: Number,
  },
  methods: {
    expandSection() {
      this.isExpanded = !this.isExpanded;
    },
  },
};
</script>

<style scoped>
div {
  display: flex;
  flex-direction: column;
  align-items: left;
  text-align: left;
  margin: 0.8rem;
  padding: 0.5rem 2rem 0.5rem 2rem;
  border-radius: 25px;
  width: v-bind(itemWidth);
  height: min-content;
  background: rgb(255, 255, 255, 0.8);
  box-shadow: 2px 2px 2px 2px rgba(205, 204, 204, 0.2);
}

.collapsed {
  background: rgba(125, 33, 103, 0.1);
  border: 1px solid rgba(125, 33, 103, 0.02);
}

.collapsed:hover {
  transform: scale(1.01);
  transition: 200ms ease-in-out;
}

.expanded {
  border: 1px solid rgba(125, 33, 103, 0.1);
}

.expanded h3 {
  margin-bottom: 0px;
}

h3:hover {
  cursor: pointer;
  text-shadow: 0 4px 4px 0 rgba(0, 0, 0, 0.2);
}
</style>
