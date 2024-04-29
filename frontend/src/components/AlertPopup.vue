<!-- eslint-disable -->
<template>
    <div class="container" v-if="type=='alert'">
        <div class="upper-section">
            <h3> Wrong File Uploaded! </h3>
            <button type="button" class="btn-close" @click="close" >  x   </button>
        </div>
        <p class="body"> Unreadable file. 
            <br> You have uploaded a file in the wrong format <br> or with the wrong information. <br>
            <br> Please insert a valid genotype file in .txt or .vcf format. </p>
    </div>

    <div class="container" v-if="type=='loading'">
      <h3> Analysing File... </h3>
      <p class="body" style="padding-bottom: 0px;"> Please wait unil the file has been analysed.
        <br> This may take several minutes. </p>
      <h2> <i> DO NOT REFRESH PAGE </i> </h2>
  </div>
</template>

<script>
export default {
  name: "AlertPopup",
  props: {
    type: String,
  },
  methods: {
    close() {
      this.$emit("close");
    },
  },
};
</script>

<style scoped>
.container {
  position: fixed;
  top: 25vh;
  display: flex;
  flex-direction: column;
  margin: 0.6rem;
  padding: 1rem 1rem 1rem 1rem;
  border-radius: 25px;
  width: 50vw;
  height: 40vh;

  background: rgba(250, 250, 250, 1);
  justify-content: center;
  align-items: center;

  border: 1px solid (125, 33, 103, 1);
  box-shadow: 0px 0px 6px 2px rgba(0, 0, 0, 0.2);
}

.upper-section {
  display: flex;
  flex-direction: row;
  text-align: left;
  justify-content: space-between;

  padding: 1rem 2rem 1rem 2rem;
  border-radius: 25px;
}

.body {
  position: relative;
  padding: 0px 10px 50px 10px;
  font-size: large;
}

.btn-close {
  position: absolute;
  top: 10px;
  right: 20px;
  border: none;
  font-size: 25px;
  padding: 10px;
  cursor: pointer;
  font-weight: bold;
  background: transparent;
  color: rgba(125, 33, 103);
}

.btn-close:hover {
  transform: scale(1.2);
}

h3 {
  font-size: x-large;
}
</style>
