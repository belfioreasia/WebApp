<!-- eslint-disable -->
<template>
  <div class="result-container">
      <div class="upper">
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
                                      itemWidth="40"> 
                            
                            <div>
                              <div v-if="index==0"> 
                                <h2 style="font-size: xx-large;"> {{parseFloat(this.score[0]).toFixed(3)}} </h2>
                                <ChartJs :data="this.chart_data[2]" 
                                                :width="40" 
                                                :height="35" 
                                                title="null"> </ChartJs>
                              </div>
                              <div v-else-if="index==1"> 
                                <h2 style="font-size: xx-large;"> {{parseFloat(this.score[1]).toFixed(3)}} </h2>
                                <ChartJs :data="this.chart_data[3]" 
                                                :width="25" 
                                                :height="35" 
                                                title="null"> </ChartJs>
                              </div>
                            </div>
                      </CarouselItem> 
                  </div>
              </div>
          </div>
          <button type="button" class="btn" @click="slideNext"> > </button> 
        </div>
          <div class="toggle-lists">
                  <ToggleList     title="What does my score mean?"
                                  :index="0"
                                  :width="30" >
                      <div class="inside-toggle-list">
                        <p v-if="(1-this.score[0])>=0.3"> 
                          Your score suggest that your genetic profile is similar to the one of individuals
                          who <strong>do not have Crohn's Disease</strong>. 
                          <br> This means that your genetic data and mutations are not relevantly linked
                          to an increased risk in Crohn's Disease.
                        </p>
                        <p v-else> 
                          Your score suggest that your genetic profile is similar to the one of individuals
                          who <strong>have Crohn's Disease</strong>. 
                          <br> This means that your genetic data and mutations are likely relevantly linked
                          to an <strong>increased risk in Crohn's Disease</strong>.
                        </p>
                      </div>
                  </ToggleList>
                  <ToggleList     title="What's the difference between the two scores?"
                                  :index="1"
                                  :width="30" > 
                      <div class="inside-toggle-list">
                        <p> The <strong>'DNN Score'</strong> is calculated using our Neural Network. 
                          <br> The <strong>'Manual PRS'</strong> score is calculated as a sum of your genetic mutations 
                          weighted by their statistical effect on the Disease. </p>
                      </div>
                  </ToggleList>
                  <ToggleList     title="How accurate are the two scores?"
                                  :index="2"
                                  :width="30" > 
                      <div class="inside-toggle-list">
                        <p> 
                          Both scores represent an <strong>estimated risk</strong> of developing the disease based only on  
                        </p>
                      </div>
                  </ToggleList>
          </div>
      </div>
    <div class="charts">
      <div class="chart-item">
      <ChartJs  :data="this.chart_data[0]" 
                :width="30" 
                :height="50" 
                 title="Mutations distribution"> </ChartJs>
      </div>
      <div class="chart-item">
      <ChartJs :data="this.chart_data[1]" 
               :width="50" 
               :height="50" 
                title="Your score in the population"></ChartJs>
      </div>
    </div>
      <footer> <p style="text-align: center;"> Discover more about <a href="https://qmul.ac.uk"> Queen Mary University of London</a>. <br>
          Discover more about <a href="https://dantelabs.com"> Dante Labs</a>.</p> </footer>
  </div>
</template>

<script>
/* eslint-disable */
import CarouselItem from "@/components/CarouselItem.vue";
import ToggleList from "@/components/ToggleList.vue";
import ChartJs from "./ChartJs.vue";
import gsap from "gsap";

export default {
name: "ResultTab",
components: {
  CarouselItem,
  ToggleList,
  ChartJs,
},
props: {
  score: Array,
  snp_list: Array,
},
data() {
  return {
    central_item: 0,
    position: 0,
    num_items: 2,
    step: 385,
    titles: ['Your Neural Network Score', 
             'Manual PRS'],
    chart_data: [this.getMutationsData("radar"),
                 this.getPRSData("bar"), 
                 // this.getMutationsData("bar"),
                 this.getScoreData("pie", this.score[0]),
                 this.getScoreData("pie", this.score[1])],
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
  getPRSDist(prs_score){
    let array_score = []
    if (prs_score<0){
      return [14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    };
    if (prs_score>1){
      return [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14]
    };
    array_score[0] = 0;
    array_score[11] = 0;
    for(let i=0;i<=10;i++){
        if((prs_score>=(i/10))&&(((i+1)/10)>prs_score)){
          array_score[i+1]=14;
        }
        else {
          array_score[i+1]=0;
        }
    };
    return array_score;
  },
  getScoreData(chart_type, score) {
    return {
        type: chart_type,
        data: {
          labels: ["Normal Risk", "Increased Risk"],
          datasets: [
            {
              type: "pie",
              data: [0.85, 0.15],
              backgroundColor: ["rgba(15, 200, 15, .3)", "rgba(200, 15,15, .5)"],
              borderWidth: 5,
              borderRadius: 8,
            },
            {
              label: 'DNN',
              type: "pie",
              data: [score, Math.abs(1-score)],
              backgroundColor: ["rgba(125, 33, 103, .8)", "rgba(192, 204, 217, .2)"],
              borderWidth: 5,
              borderRadius: 10,
            },
          ]
        },
        options: {
          responsive: false,
          cutout: [80, 60],
          rotation: -90,
          circumference: 58 * Math.PI,
        }
    };
  },
  getMutationsData(chart_type) {
    return {
      type: chart_type,
      data: {
        labels: ["Chr1","Chr2","Chr3","Chr4","Chr5","Chr6","Chr7","Chr8","Chr9","Chr10",
                  "Chr11","Chr12","Chr13","Chr14","Chr15","Chr16","Chr17","Chr18","Chr19",
                  "Chr20","Chr21","Chr22",],
        datasets: [
          {
            label: "Your Data",
            data: this.snp_list,
            backgroundColor: "rgba(125, 33, 103, .8)",
            borderColor: "rgba(125, 33, 103, .8)",
            borderWidth: 1.5,
          },
          {
            label: "Base Data",
            data: [20, 15, 10, 6, 10, 4, 3, 8, 6, 5, 10, 5, 6, 4, 3, 5, 4, 5, 7, 5, 3, 3],
            backgroundColor: "rgba(192, 204, 217, .4)",
            borderColor: "rgba(192, 204, 217, .8)",
            borderWidth: 2,
          },
        ],
      },
      options: {
        responsive: true,
        lineTension: 0,
      },
    };
  },
  getPRSData(chart_type) {
    return {
      type: chart_type,
      data: {
        labels: ["<0","0<_<.1",".1<_<.2",".2<_<.3",".3<_<.4",".4<_<.5",".5<_<.6",
                  ".6<_<.7",".7<_<.8",".8<_<.9",".9<_<1", ">1"],
        datasets: [
          {
            label: "Your Score: "+ parseFloat((this.score[1])).toFixed(3),
            type: "bar",
            data: this.getPRSDist(this.score[1]),
            backgroundColor: "rgba(125, 33, 103, .9)",
            borderColor: "rgba(125, 33, 103, .8)",
            borderWidth: 0,
            barThickness: 20,
          },
          {
            label: "Cases Distribution",
            type: "line",
            data: [1, 2, 3, 7, 11, 14, 12, 10, 9, 6, 3, 1], 
            backgroundColor: "rgba(200, 15,15, .2)",
            borderColor: "rgba(200, 15,15, .2)",
            borderWidth: 3,
            pointStyle: false,
          },
          {
            label: "Controls Distribution",
            type: "line",
            data: [1, 3, 4, 9, 14, 12, 10, 8, 5, 3, 1, 1],
            backgroundColor: "rgba(192, 204, 217, .2)",
            borderColor: "rgba(192, 204, 217, .8)",
            borderWidth: 3,
            pointStyle: false,
          },
        ],
      },
      options: {
        responsive: true,
        lineTension: 0.5,
      },
    };
  },
},
};
</script>

<style scoped>
.result-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0.2vh 1vw 1vh 1vw;
  height: 80vh;
}

.upper {
  display: flex;
  flex-direction: row;
  gap: 0%;
}

.toggle-lists {
  display: flex;
  flex-direction: column;
  place-content: center;
}

.carousel-section {
  display: flex;
  flex-direction: row;
  align-items: center;
  margin: 0px;
  width: 50vw;
}

.carousel-container {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 2vw;

  width: 37vw;
  overflow-x: hidden;
}

.carousel {
  position: relative;
  display: flex;
  flex-wrap: wrap;
  place-items: center;

  margin-top: 0.1vh;
  margin-bottom: 0.5vh;
  inset-inline-start: 3vw;
}

.carousel-item {
  display: flex;
  flex-direction: column;
  place-items: center;
  gap: 0px;
  padding-bottom: 2vh;
}

::-webkit-scrollbar {
  display: none;
}

.btn {
  height: 30px;
  width: 40px;
  padding: 10px 10px 27px 10px;
  border-radius: 15px;
  font-weight: bolder;
}

.inner-carousel-slot {
  place-content: center;
}

h2 {
  margin-bottom: 0px;
  margin-top: 1vh;
}

p {
  text-align: justify;
}

.charts {
  display: flex;
  flex-direction: row;
  gap: 2vw;
  padding-top: 2vh;
}

.chart-item {
  border: 1px solid rgb(125, 33, 103);
  border-radius: 25px;
  justify-content: center;
  height: fit-content;
  width: fit-content;
}

footer {
  margin-top: 1vh;
}
</style>
