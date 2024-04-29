<!-- eslint-disable -->
<template>
  <nav>
    <div class="nav"> 
      <router-link to="/" class="link"> <img class="left-img" alt="Dante Labs logo" src="@/assets/dantelabs.png"/> </router-link>
      <div class="links">
        <router-link to="/"> <button class="btn"> Home </button> </router-link> 
        <!-- <router-link to="/neural-network"> <button class="btn/"> Our Research </button> </router-link>  -->
        <router-link to="/our-research"> <button class="btn"> Our Research </button> </router-link> 
        <router-link to="/pred"> <button class="btn"> Get a Prediction </button> </router-link>  
        <!-- <router-link to="/crohn"> <button class="btn"> Crohn's Disease </button> </router-link> -->
      </div>
      <router-link to="/" class="link"> <img class="right-img" alt="QMUL logo" src="@/images/qmul.png"/> </router-link>
    </div>
    </nav>
  <router-view />
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  font-size: 15px;
  color: rgba(125, 33, 103);
  height: 100vh;
  width: 100vw;
  /* color: rgb(72, 71, 73);*/
}

h1 {
  margin-top: 1vh;
  margin-bottom: 0px;
}

a {
  color: rgba(125, 33, 103);
  font-weight: 500;
  font-style: italic;
  text-decoration: none;
  cursor: pointer;
}

strong {
  color: rgba(125, 33, 103);
  font-style: italic;
}

b {
  color: rgba(125, 33, 103);
}

p {
  text-align: center;
  color: rgb(72, 71, 73);
}

.nav {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
  padding: 10px;

  border-bottom: 1px solid rgba(125, 33, 103);
  background-color: rgb(244, 244, 245, 0.5);
  margin-left: 0px;
}

.left-img {
  height: 40px;
  width: auto;
  position: absolute;
  left: 50px;
  top: 25px;
}

.right-img {
  height: 40px;
  width: auto;
  position: absolute;
  right: 50px;
  top: 25px;
}

.left-img:hover,
.right-img:hover {
  transform: scale(1.1);
  transition: 200ms ease-in-out;
  cursor: pointer;
}

.btn {
  border-radius: 25px;
  background-color: rgb(244, 244, 245, 1);
  border: 1px solid rgb(125, 33, 103, 1);
  color: rgb(125, 33, 103);

  font-size: 15px;
  margin: 1vw;
  padding: 1.2vh 1.5vw 1.2vh 1.5vw;
  text-align: center;
  transition: all 200ms;
}

.btn:hover {
  cursor: pointer;
  background-color: rgb(125, 33, 103);
  color: #fff;
  box-shadow: 0 4px 4px 0 rgba(0, 0, 0, 0.2);
}
</style>
