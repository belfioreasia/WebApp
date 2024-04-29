<!-- eslint-disable -->
<template>
    <div class="inner-carousel-slot">
        <p style="margin-bottom: 0px"> This service was created as part of an Undergraduate
        <strong>EECS Final Year Project</strong>, with the goal of bridging the gap between the Technological advancements
        and personalised medicine. The project's strength comes from the harmonious combination of QMUL's Technological 
        Resources and Dante Labs' expertise in the Genomics field.
        </p> 
        <SummaryBand :icons=this.icons
                    :titles=this.titles
                    :bodies=this.bodies
                    width=14
                    height=8 
                    color="rgba(125, 33, 103)"/>
        <p style="margin-top: 0px"> 
        
        </p>        
          <div class="middle-images">
            <img alt="our Deep Neural Network" src="@/images/genetic_mutations.png" style="width: 40vw;"/>   
            <p style="width: 20vw;"> Personalised Disease Prediction is based on the analysis of <strong>genetic mutations</strong>
              present in one's DNA. These often take the form of <i>Single Nucleotide Polymorphisms</i>, changes in a specific sequence
              of DNA bases, like <strong>A>G</strong>. 
              <br> These mutations can affect many biological behaviours, like protein synthetsis and immune response.
              <br> Some mutations can <strong>influence the probability</strong> that the individual develops a certain disease,
              like <strong>Crohn's Disease</strong>.

              </p>    
        </div>
        <div class="middle-images">
          <p style="width: 20vw;"> The <strong>Crohn's Pred</strong> Neural Network analyses <i>147</i> Single Nucleotide Polymorphisms
            linked to Crohn's Disease, spanning from Chromosome 1 to Chromosome 22.
            <br> It predicts your the genetic risk score (between 0 and 1) based on the frequency of each of the 147 mutations
            present in your DNA.
            </p>  
            <img alt="The DNN" src="@/images/DNN.png" style="width: 40vw;"/>
        </div>                                        
    </div>
</template>

<script>
/* eslint-disable */
import SummaryBand from '@/components/SummaryBand.vue'

export default {

  name: "ProjectPage",
  components: {
    SummaryBand,
  },
  data() {
    return{
      icons: ["star.png", "dna.png", "health.png", "location.png"],
      titles: ['8 Months', '160000+' , 'Synthetic Data', "⬤⬤⬤◯◯"], 
      bodies: ['of Research Time', 'Samples Analysed', 'for Data Privacy', '64% Accuracy'],
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

.middle-images{
  margin-top: 3vh;
  display: flex;
  gap: 1em;
  }
  
  .middle-images img {
  border-radius: 10px;

  transition: transform 300ms ease-in-out;
  }
  
  .middle-images img:hover{
    transform: scale(1.05);
    box-shadow: 2px 2px 2px 2px rgba(205, 204, 204, 0.5);
  }


</style>
