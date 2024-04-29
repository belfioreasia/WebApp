<!-- eslint-disable -->
<template>
  <div class="home">
    <h1> Neural Network for <i>Crohn's Disease</i> Prediction </h1>
    <p style="margin-bottom: 0px;">A <b>Dante Labs</b> <i>x</i> <b>Queen Mary University</b> of London Project. </p> 
    <!-- main carousel section with 3 components: 
              1 - Dante Labs Page
              1 - Queen Mary Page
              1 - Project Page  -->
    <div class="carousel-section">
        <!-- Backwards button -->
        <button type="button" class="btn" @click="slidePrevious"> < </button>
        <div class="carousel-container">
            <div class="carousel" v-for="(title, index) in this.carousel_titles" :key="index">
                <div class="carousel-item">
                    <!-- Loop to render all components -->
                    <h2 v-if="index==this.central_item"> {{title}} </h2>
                    <CarouselItem   :index="(index)" 
                                    :title="title"
                                    :isCentral="(index)==this.central_item" 
                                    maxHeight="55"
                                    itemWidth="110"> 
                          <!-- Render page contents based on carousel central item -->
                          <div>
                            <!-- Dante Labs page (default) -->
                            <div v-if="index==0" class="inner-carousel-slot"> 
                              <DantePage />
                            </div>
                            <!-- QMUL page -->
                            <div v-else-if="index==1" class="inner-carousel-slot"> 
                              <QMULPage/>
                            </div>
                            <!-- Project page -->
                            <div v-else-if="index==2" class="inner-carousel-slot"> 
                              <ProjectPage/>
                            </div>
                          </div>
                    </CarouselItem> 
                </div>
            </div>
        </div>
        <!-- Forward button -->
        <button type="button" class="btn" @click="slideNext"> > </button> 
    </div>
    <div class="slide-bottom-panel">
      <div v-for="index in this.num_items">
        <button v-if="(index-1)==central_item" type="button" class="slide-btn-current">  </button> 
        <button v-else type="button" class="slide-btn-else" @click="takeStep(index-1)">  </button> 
      </div>
    </div>
    <footer> 
      <!-- Render information based on which carousel item is central to match inner page information. -->
      <p v-if="central_item==0"> Discover more about <a href="https://dantelabs.com"> Dante Labs</a>. </p> 
      <p v-if="central_item==1"> Discover more about <a href="https://qmul.ac.uk"> Queen Mary University of London</a>.</p>
      <p v-if="central_item==2"> Discover more about <router-link to="/our-research" class="link">our Research</router-link>.</p> 
    </footer>
  </div>
</template>

<script>
/* eslint-disable */
import CarouselItem from '@/components/CarouselItem.vue';
import SummaryBand from '@/components/SummaryBand.vue';
import DantePage from '@/components/DantePage.vue'
import QMULPage from '@/components/QMULPage.vue';
import ProjectPage from '@/components/ProjectPage.vue';
import gsap from 'gsap';

export default {
  name: "HomeView",
  components: {
    CarouselItem,
    SummaryBand,
    DantePage,
    QMULPage,
    ProjectPage,
  },
  data() {
    return{
      central_item: 0,
      position: 0,
      num_items: 3,
      step: 380,
      carousel_titles: ["Dante Genomics", "Queen Mary University of London", "Neural Network for Disease Prediction"],
    };
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
  },
};
</script>

<style scoped>

.home {
  display: flex;
  flex-direction: column;
  height: 100vh;
  align-items: center;
  padding: 1rem;
  background-color: rgb(244, 244, 245, 1);
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

    margin-top: 0.1vh;
    margin-bottom: 0.5vh;
    inset-inline-start: 2.5vw;
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

.slide-bottom-panel {
  display: flex;
  gap: 1rem;
}

.slide-btn-else,
.slide-btn-current {
  margin-top: 2vh;
  height: 17px;
  width: 17px;
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

footer {
  margin-top: 1rem;
}

</style>
