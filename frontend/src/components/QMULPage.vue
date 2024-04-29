<!-- eslint-disable -->
<template>
    <div class="inner-carousel-slot">
      <div class="middle-images">
        <img class="header-img" alt="QMUL" src="@/images/Queens-Building.jpg" style="width: 43vw;"/>
        <img class="header-img" alt="QMUL" src="@/images/qmul-logo.gif" style="width: 23vw;"/>
      </div>
      <p> <strong>Queen Mary University of London</strong> is one of the UK's leading 
        research universities, committed to improving social justice and achieving the previously unthinkable.
      <br> In 2012, the University joined the prestigious <strong>Russel Group</strong> and in 2021, 
      Queen Mary became the first UK university to receive the Platinum-level Engage Watermark from the 
      National Co-ordinating Centre for Public Engagement.
      </p>                                                  
      <SummaryBand :icons=this.icons
                  :titles=this.titles
                  :bodies=this.bodies
                  width=15
                  height=8
                  color="rgb(35, 37, 145)" />
      <div class="middle-images">
          <img alt="QMUL" src="@/images/london-view.jpg" />
          <img alt="QMUL" src="@/images/Library.jpg" />
          <img alt="QMUL" src="@/images/Fogg-Building.jpg"/>
      </div>
    </div>

    
</template>

<script>
/* eslint-disable */
import SummaryBand from '@/components/SummaryBand.vue'

export default {

  name: "QMULPage",
  components: {
    SummaryBand,
  },
  data() {
    return{
      icons: ["russel_group.png", "globe.png", "pin.png"],
      titles: ['Russel Group', '14th globally', '5th in the UK'],
      bodies: ['University Member', 'for Research quality', 'for Research quality'],
    };
  },
};

</script>

<style scoped>

.inner-carousel-slot {
  display: flex;
  flex-direction: column;
  align-items: center;
}

strong {
  color: rgb(35, 37, 145);
}

.inner-carousel-slot p{
  text-align: justify;
  padding: 1vw 1vw 0px 1vw;
  width: 62vw;
}

.header-img {
  width: 60vw;
  left: 0px;
  border-radius: 25px;
}

.middle-images{
margin-top: 3vh;
display: flex;
gap: 1em;
}

.middle-images img {
border-radius: 10px;
width: 20vw;
transition: transform 300ms ease-in-out;
}

.middle-images img:hover{
  transform: scale(1.05);
  box-shadow: 2px 2px 2px 2px rgba(205, 204, 204, 0.5);
}

</style>

