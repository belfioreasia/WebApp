<!-- eslint-disable -->
<template>
  <div class="page-container">
    <h1> Our Research </h1>
    <p> Discover more about our research on the applications of Neural Networks for 
      <router-link to="/pred" class="link">Crohn's Disease Prediction:</router-link></p>
    <div class="info-container"> 
      <div class="carousel-section">
        <button type="button" class="btn" @click="slidePrevious"> < </button>
        <div class="carousel-container">
            <div class="carousel" v-for="(title, index) in this.titles" :key="index">
                <div class="carousel-item">
                    <h2 v-if="index==this.central_item"> {{title}} </h2>
                    <CarouselItem   :index="(index)" 
                                    :title="title"
                                    :isCentral="(index)==this.central_item" 
                                    maxHeight="45"
                                    itemWidth="90"> 
                          <div v-if="index==0">
                            <div class="toggle-lists">
                              <ToggleList
                                title="What is Crohn's Disease?"
                                :index="0"
                                :width="this.toggle_item_width">
                                  <div class="inside-toggle-list">
                                    <p> <strong>Crohn's disease</strong> is a type of inflammatory bowel disease (IBD). 
                                      <br> It causes inflammation in any part of the digestive tract, which can lead to abdominal pain, diarrhea, fatigue, and malnutrition.
                                      <img style="float: right; width: 20vw; margin: 5px 0px 5px 10px;" src="@/images/cd-symptoms.jpeg"> 
                                      <br> Crohn's can occur at any age, with around <strong>20% of affected people</strong> being diagnosed before the age of 18 
                                          and nearly <strong>6%</strong> after the age of 60.
                                      <br> Oral Treatment is usually prescribed with medications such as <strong>Mesalazina</strong>, but these can only
                                          help in easing the Disease symptoms and to keep flares aat a minimum.
                                          <br> If you think you may have any of these symptoms, <strong>please consult your GP</strong>.
                                      </p>
                                  </div>
                              </ToggleList>
                              <ToggleList
                                title="What is the link between Crohn's Disease and genetics?"
                                :index="1"
                                :width="this.toggle_item_width">
                                  <div class="inside-toggle-list">
                                    <p> Although the exact causes of Crohn's Disease are not yet clear, it is estimated that around <strong>13%</strong> 
                                      of Crohn's liability can be traced back to genetic factors.  
                                      <img style="float: left; width: 25vw; margin: 5px 10px 5px 0px;" src="@/images/causes-crohns.png"> 
                                      <br> Many studies have been able to link over <strong>140 genetic mutations</strong> to an increased
                                          risk of developing Crohns Disease.
                                       <br> Notable mutations include variants on the <strong>NOD2</strong> gene, on the 16th Chromosome.
                                       <br> Other influencial factors include <strong>smoking</strong>, which as far as <strong>triplicates</strong>
                                        the risk of Crohn's and its severity, as well as diet and stress.
                                      </p>
                                  </div>
                              </ToggleList>
                              <ToggleList
                                title="How is this research linked to Crohn's Disease?"
                                :index="2"
                                :width="this.toggle_item_width">
                                  <div class="inside-toggle-list">
                                    <img style="float: right; width: 25vw; margin: 5px 10px 5px 0px;" src="@/images/cd-panel.png"> 
                                    <p> The implemented Neural Network was trained in order to be able to recognize <strong>patterns in genetic profiles</strong> of
                                      individuals with Crohn's. 
                                      <br> This allows the Network to distringuish (still shyly) between <strong>case</strong> patients, who have the Disease,
                                      and <strong>control</strong> healthy individual.
                                       <br> If you would like to get a prediction, please ensure you have a genetic test result file ready in <strong>VCF format</strong>
                                       <br> If you have not yet taken a Genetic Test and would like to know more, please visit the 
                                       <a href="https://www.dantelabs.com/products/crohn-disease-panel">Dante Labs</a> Crohn's Panel Test.
                                      </p>
                                  </div>
                              </ToggleList>
                            </div>
                          </div>
                          <div v-else>
                          <div class="toggle-lists">
                              <ToggleList
                                title="What are Neural Networks?"
                                :index="0"
                                :width="this.toggle_item_width">  
                                  <div class="inside-toggle-list">
                                    <p> <strong>Neural Networks</strong> are a subclass of Machine Learning models </p>
                                    <img style="float: right; width: 25vw; margin: 5px 10px 5px 0px;" src="@/images/ai_vs_dl.png">
                                  </div>
                              </ToggleList>
                              <ToggleList 
                                title="How are they used in Disease Prediction?"
                                :index="1"
                                :width="this.toggle_item_width">  
                                  <div class="inside-toggle-list">
                                    <p> Neural Networks are  </p>
                                    <img src="@/images/DNN.png">
                                  </div>
                              </ToggleList>
                              <ToggleList 
                                title="Our Network: Crohn's Predict"
                                :index="2"
                                :width="this.toggle_item_width">  
                                  <div class="inside-toggle-list">
                                    <p> Neural Networks are  </p>
                                    <img src="@/images/DNN.png">
                                  </div>
                              </ToggleList>
                          </div>
                        </div>
                    </CarouselItem> 
                </div>
            </div>
        </div>
        <button type="button" class="btn" @click="slideNext"> > </button> 
      </div>
    </div>
    <div class="slide-bottom-panel">
      <div v-for="index in this.num_items">
        <button v-if="(index-1)==central_item" type="button" class="slide-btn-current">  </button> 
        <button v-else type="button" class="slide-btn-else" @click="takeStep(index-1)">  </button> 
      </div>
    </div>
    <p v-if="central_item==1"> More on Neural Networks 
      <a href="https://www.sciencedirect.com/journal/neural-networks"> here</a>: 
      <br> Learn more about our Research Implementation 
      <a href="https://www.github.com/belfioreasia/CrohnsPred"> here</a>: </p>
    <p v-else-if="central_item==0"> Learn more about Crohn's Disease 
      <a href="https://www.dantelabs.com/products/crohn-disease-panel"> here</a>: 
    <br> Source: <a href="https://crohnsandcolitis.org.uk">Crohn's and colitis UK</a>
     </p>

  </div>
</template>

<script>
/* eslint-disable */
import ToggleList from '@/components/ToggleList.vue'
import CarouselItem from '@/components/CarouselItem.vue';
import gsap from 'gsap';

export default {
  name: "ResearchView",
  components:{
    ToggleList,
    CarouselItem,
  },
  data() {
    return{
      central_item: 0,
      position: 0,
      num_items: 2,
      step: 385,
      titles: ["Crohn's Disease",
              "The Neural Network"],
      toggle_item_width: 45,
    }
  },
  methods: {
    slideNext() {
      if (this.central_item >= this.num_items - 1) {
        this.takeStep(0)
      } else {
        this.takeStep(this.central_item+1)
      }
    },

    slidePrevious() {
      if (this.central_item <= 0) {
        this.takeStep(this.num_items - 1)
      } else {
        this.takeStep(this.central_item-1)
      }
    },

    takeStep(new_center) {
      let items_to_skip = Math.abs(this.central_item - new_center)
      if (this.central_item > new_center) {
        this.position += (this.step * (items_to_skip));
      } 
      else {
        this.position -= (this.step * (items_to_skip));
      }
      this.central_item = new_center;
      gsap.fromTo(
          ".carousel",
          { scale: 0.8 },
          { x: this.position, scale: 1 }
        );
    },
  }
};
</script>

<style scoped>
.page-container{
  display: flex;
  flex-direction: column;
  place-items: center;
  padding-top: 5vh;
  height: 100%;
  background-color: rgb(244, 244, 245, 0.5);
}

.info-container {
  display: flex;
  place-content: center;
  gap: 1.5vw;
}

.carousel-section {
  display: flex;
  flex-direction: row;
  align-items: center;
  margin: 0px;
  width: 90vw;
}

.carousel-container {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 2vw;

  width: 80vw;
  overflow-x: hidden;

}

.carousel {
  position: relative;
  display: flex;
  flex-wrap: wrap;
  place-items: center;

  margin-top: 0px;
  margin-bottom: 0.5vh;
  inset-inline-start: 10vw;
}

.carousel-item {
  display: flex;
  flex-direction: column;
  place-items: center;
}

::-webkit-scrollbar {
  display: none;
}

.btn {
  height: 30px;
  width: 40px;
  padding: 10px 10px 27px 10px;
  border-radius: 5px;
  font-weight: bolder;
}

.toggle-lists {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: left;
}

.slide-bottom-panel {
  display: flex;
  gap: 1rem;
}

.slide-btn-else,
.slide-btn-current {
  margin-top: 2vh;
  height: 20px;
  width: 20px;
  border-radius: 100px;
  border: 1px solid rgb(125, 33, 103, 1);
}

.slide-btn-current {
  background-color: rgb(125, 33, 103, 1);
}

.slide-btn-current:hover,
.slide-btn-else:hover {
  cursor: pointer;
  background-color: rgb(125, 33, 103, 0.8);
  color: #fff;
  box-shadow: 0 4px 4px 0 rgba(0, 0, 0, 0.2);
}

h2 {
  margin: 2vh;
}

p {
  text-align: justify;
  font-size: 16px;
}

img {
  width: 40vw;
  height: auto;
}
</style>
