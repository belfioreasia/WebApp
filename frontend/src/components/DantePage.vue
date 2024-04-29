<!-- eslint-disable -->
<template>
    <div class="inner-carousel-slot">
        <img class="header-img" alt="QMUL" src="@/images/DNA-dl.png" style="width: 68.5vw;" />
        <p style="margin-bottom: 0px"> <strong>Dante Genomics</strong> is a leading global genomics and precision medicine company working to accelerate science 
        to deliver better healthcare and ultimately save lives with a more human approach to health. 
        Their mission is to leverage whole genome sequencing technology and variant interpretation, 
        so that you can make informed decisions about your health and your future.
        </p> 
        <SummaryBand :icons=this.icons
                    :titles=this.titles
                    :bodies=this.bodies
                    width=15
                    height=8 
                    color="rgba(125, 33, 103)"/>
        <p style="margin-top: 0px"> Dante leverages expertise in science and healthcare to create customized genomic analysis processes 
          that have an impact on people's lives.
          Dante's <strong>Whole Genome Sequencing</strong> services offer genetic tests that can decipher your entire DNA, with <strong>30x coverage</strong>, 
          meaning your entire genome will be analyzed 30 times, picking up more valuable genomic information with each pass.
        </p>   
        <div class="middle-images">
          <div class="left-images">
            <img alt="Sequencing Device" src="@/images/NovaSeq.jpg"/>
            <img alt="Dante Founders" src="@/images/DL-founders.jpeg"/>
          </div>
          <img alt="Dante Employee" src="@/images/DL-employee.png" style="width: 25vw; "/>
        </div>  
        <p> <strong>Dante Genomics</strong> is a leading global genomics and precision medicine company working to accelerate science 
          to deliver better healthcare and ultimately save lives with a more human approach to health. 
          Their mission is to leverage whole genome sequencing technology and variant interpretation, 
          so that you can make informed decisions about your health and your future.
          </p>                                                        
    </div>
</template>

<script>
/* eslint-disable */
import SummaryBand from '@/components/SummaryBand.vue'

export default {

  name: "DantePage",
  components: {
    SummaryBand,
  },
  data() {
    return{
      icons: ["dna.png", "star.png", "location.png"],
      titles: ['300000+ ', '4.2 ★★★★☆', '97 Countries'], 
      bodies: ['Kits Analysed', 'Customer Reviews', 'Service Availablity'],
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

.middle-images img:hover{
  transform: scale(1.03);
}

.middle-images{
  display: flex;
  gap: 2em;
}

.middle-images img {
  border-radius: 10px;
  transition: transform 300ms ease-in-out;
  box-shadow: 2px 2px 2px 2px rgba(205, 204, 204, 0.5);
}

.left-images {
  display: flex;
  align-content: left;
  flex-direction: column;
  width: 35vw;
  gap: 1em;
}

</style>
