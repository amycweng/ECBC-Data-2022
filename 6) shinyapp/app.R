#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
library(bslib)



# Define UI for application that draws a histogram
ui <- navbarPage(
  # Title of shiny app
  title = "ECBC Data+ 2022",
  theme = bs_theme(version = 4, bootswatch = "sketchy"),
  collapsible = TRUE,
  tags$head(tags$style("#test .modal-dialog {width: fit-content !important;}")),
  
    # Sidebar with a slider input for number of bins
    tabPanel("Social Networks",
    sidebarLayout(
        sidebarPanel(
          selectInput("topic1", "Topic", 
                      choices = c("Tobacco", 
                                  "Opium")),
          selectInput("time1", "Time Period", 
                      choices = c("1580-1599", 
                                  "1600-1607",
                                  "1608-1617",
                                  "1618-1624", 
                                  "1625-1634", 
                                  "1635-1638",
                                  "1639-1641")),
          actionButton("run1", "View Network"),
          h6("For detailed network documentation please see the Documentation panel!"),
          h6("Below are histograms showing number of texts for each time period based on a specific topic. Use them to help you make the selections!"),
          uiOutput("tobaccohist"),
          uiOutput("opiumhist"),
          h6("Note: Some networks are big and need some time to load.")
        ),

        # Show a plot of the generated distribution
        mainPanel(
          htmlOutput("network")
        )
    )
),

tabPanel("Documentation",
         sidebarLayout(
           sidebarPanel(
             selectInput("topic2", "Topic", 
                         choices = c("Tobacco", 
                                     "Opium")),
             selectInput("time2", "Time Period", 
                         choices = c("1580-1599", 
                                     "1600-1607",
                                     "1608-1617",
                                     "1618-1624", 
                                     "1625-1634", 
                                     "1635-1638",
                                     "1639-1641")),
             actionButton("run2", "View Detailed Documentation"),
             actionButton("run3", "View Graph of Clusters"),
             h4(" "),
             htmlOutput("sidedoc")
           ),
           
           # Show a plot of the generated distribution
           mainPanel(
             htmlOutput("detail")
           )
         )
),

tabPanel("Part of Speech",
         sidebarLayout(
           sidebarPanel(
             selectInput("topic3", "Topic", 
                         choices = c("Tobacco", 
                                     "Opium")),
             selectInput("word", "Type", 
                         choices = c("Nouns", 
                                     "Adjectives",
                                     "Verbs",
                                     "Adverbs")),
             actionButton("run4", "View Word Associations")
           ),
           
           # Show a plot of the generated distribution
           mainPanel(
             uiOutput("association")
           )
         )
),

tabPanel("Word Embeddings",
         sidebarLayout(
           sidebarPanel(
             selectInput("term", "Terms", 
                         choices = c("colonialism", 
                                     "custom",
                                     "gender",
                                     "intoxicate",
                                     "medical",
                                     "moral",
                                     "ethnicities",
                                     "religion")),
             actionButton("run5", "View Word Embeddings"),
             h4(" "),
             h5("Words with highest similarity scores to tobacco over time"),
             h6("Period 1: [('sarcaparillia', 0.822), ('sublimate', 0.815)]"),
             h6("Period 2: [('tobacconist', 0.755), ('fume', 0.744)]"),
             h6("Period 3: [('allome', 0.749), ('fishmonger', 0.738)]"),
             h6("Period 4: [('importation', 0.791), ('allome', 0.772)]"),
             h6("Period 5: [('retail', 0.782), ('malt', 0.759)]"),
             h5("Words with highest similarity scores to opium over time"),
             h6("Period 1: [('astringent', 0.886), ('diaphoretical', 0.880)]"),
             h6("Period 2: [('henbane', 0.845), ('opiate', 0.817)]"),
             h6("Period 3: [('anodyne', 0.844), ('laudanum', 0.834)]"),
             h6("Period 4: [('scammony', 0.889), ('poppey', 0.881)]"),
             h6("Period 5: [('poppey', 0.864), ('mithridate', 0.843)]")
           ),
           
           # Show a plot of the generated distribution
           mainPanel(
             uiOutput("embedt"),
             uiOutput("embedo")
           )
         )
)

    
)

# Define server logic
server <- function(input, output, session) {
  
  #Update year selector based on topic selection
  observeEvent(input$topic1,{
    if(input$topic1 == "Opium"){
      updateSelectInput(
        session,
        "time1",
        choices = c("1580-1599",
                    "1600-1617",
                    "1618-1624",
                    "1625-1634",
                    "1635-1641"
        )
      )
    }
    if(input$topic1 == "Tobacco"){
      updateSelectInput(
        session,
        "time1",
        choices = c("1580-1599", 
                    "1600-1607",
                    "1608-1617",
                    "1618-1624", 
                    "1625-1634", 
                    "1635-1638",
                    "1639-1641"
        )
      )
    }
  })
  
  observeEvent(input$topic2,{
    if(input$topic2 == "Opium"){
      updateSelectInput(
        session,
        "time2",
        choices = c("1580-1599",
                    "1600-1617",
                    "1618-1624",
                    "1625-1634",
                    "1635-1641"
        )
      )
    }
    if(input$topic2 == "Tobacco"){
      updateSelectInput(
        session,
        "time2",
        choices = c("1580-1599", 
                    "1600-1607",
                    "1608-1617",
                    "1618-1624", 
                    "1625-1634", 
                    "1635-1638",
                    "1639-1641"
        )
      )
    }
  })

 
#Helper functions
  getnetwork = function(){
    if (input$topic1 == "Tobacco"){
      if (input$time1 == "1580-1599"){
        src = "www/tobaccoPeriod1Network.html"
      }
      if(input$time1 == "1600-1607"){
        src = "www/tobaccoPeriod2Network.html"
      }
      if(input$time1 == "1608-1617"){
        src = "www/tobaccoPeriod3Network.html"
      }
      if(input$time1 == "1618-1624"){
        src = "www/tobaccoPeriod4Network.html"
      }
      if(input$time1 == "1625-1634"){
        src = "www/tobaccoPeriod5Network.html"
      }
      if(input$time1 == "1635-1638"){
        src = "www/tobaccoPeriod6Network.html"
      }
      if(input$time1 == "1639-1641"){
        src = "www/tobaccoPeriod7Network.html"
      }
    }
    
    if(input$topic1 == "Opium"){
      if (input$time1 == "1580-1599"){
        src = "www/opiumPer1Network.html"
      }
      if(input$time1 == "1600-1617"){
        src = "www/opiumPer2Network.html"
      }
      if(input$time1 == "1618-1624"){
        src = "www/opiumPer3Network.html"
      }
      if(input$time1 == "1625-1634"){
        src = "www/opiumPer4Network.html"
      }
      if(input$time1 == "1635-1641"){
        src = "www/opiumPer5Network.html"
      }
    }
    
    return(src)
  }
  
  getdoc = function(){
    if (input$topic2 == "Tobacco"){
      if (input$time2 == "1580-1599"){
        src = "www/tobaccoPer1doc.html"
      }
      if(input$time2 == "1600-1607"){
        src = "www/tobaccoPer2doc.html"
      }
      if(input$time2 == "1608-1617"){
        src = "www/tobaccoPer3doc.html"
      }
      if(input$time2 == "1618-1624"){
        src = "www/tobaccoPer4doc.html"
      }
      if(input$time2 == "1625-1634"){
        src = "www/tobaccoPer5doc.html"
      }
      if(input$time2 == "1635-1638"){
        src = "www/tobaccoPer6doc.html"
      }
      if(input$time2 == "1639-1641"){
        src = "www/tobaccoPer7doc.html"
      }
    }
    
    if(input$topic2 == "Opium"){
      if (input$time2 == "1580-1599"){
        src = "www/opiumPer1doc.html"
      }
      if(input$time2 == "1600-1617"){
        src = "www/opiumPer2doc.html"
      }
      if(input$time2 == "1618-1624"){
        src = "www/opiumPer3doc.html"
      }
      if(input$time2 == "1625-1634"){
        src = "www/opiumPer4doc.html"
      }
      if(input$time2 == "1635-1641"){
        src = "www/opiumPer5doc.html"
      }
    }
    
    return(src)
  }
  
  getcluster = function(){
    addResourcePath("www", "www")
    if (input$topic2 == "Tobacco"){
      if (input$time2 == "1580-1599"){
        src = "www/tobaccoper1cluster.png"
      }
      if(input$time2 == "1600-1607"){
        src = "www/tobaccoper2cluster.png"
      }
      if(input$time2 == "1608-1617"){
        src = "www/tobaccoper3cluster.png"
      }
      if(input$time2 == "1618-1624"){
        src = "www/tobaccoper4cluster.png"
      }
      if(input$time2 == "1625-1634"){
        src = "www/tobaccoper5cluster.png"
      }
      if(input$time2 == "1635-1638"){
        src = "www/tobaccoper6cluster.png"
      }
      if(input$time2 == "1639-1641"){
        src = "www/tobaccoper7cluster.png"
      }
    }
    
    if(input$topic2 == "Opium"){
      if (input$time2 == "1580-1599"){
        src = "www/opiumPer1Cluster.png"
      }
      if(input$time2 == "1600-1617"){
        src = "www/opiumPer2Cluster.png"
      }
      if(input$time2 == "1618-1624"){
        src = "www/opiumPer3Cluster.png"
      }
      if(input$time2 == "1625-1634"){
        src = "www/opiumPer4Cluster.png"
      }
      if(input$time2 == "1635-1641"){
        src = "www/opiumPer5Cluster.png"
      }
    }
    
    return(src)
  }
  
  getasso = function(){
    if(input$topic3 == "Tobacco"){
      if(input$word == "Nouns"){
        src = "www/tobn.png"
      }
      if(input$word == "Adjectives"){
        src = "www/tobadj.png"
      }
      if(input$word == "Verbs"){
        src = "www/tobv.png"
      }
      if(input$word == "Adverbs"){
        src = "www/tobadv.png"
      }
    }
    
    if(input$topic3 == "Opium"){
      if(input$word == "Nouns"){
        src = "www/opn.png"
      }
      if(input$word == "Adjectives"){
        src = "www/opadj.png"
      }
      if(input$word == "Verbs"){
        src = "www/opv.png"
      }
      if(input$word == "Adverbs"){
        src = "www/opadv.png"
      }
    }
    
    return(src)
  }
  
# Display network based on selections
  observeEvent(input$run1, {
    output$network = renderUI({
      addResourcePath("www", "www")
      tags$iframe(
        seamless = "seamless",
        src = getnetwork(),
        height = 1000,
        width = 900)
    })
    })

# Display documentations based on selections
  observeEvent(input$run2, {
        output$detail = renderUI({
          addResourcePath("www", "www")
          tags$iframe(
            seamless = "seamless",
            src = getdoc(),
            height = 800,
            width = 900)
        })
  })
  
# Display word associations based on selections
  observeEvent(input$run4, {
    output$association = renderUI({
      addResourcePath("www", "www")
      img(src = getasso(),
          height="70%",
          width="80%")
    })
  })
  
# Display word embeddings based on selections
  observeEvent(input$run5, {
    output$embedt = renderUI({
      addResourcePath("www", "www")
      img(src = paste0(input$term, "Tobacco", ".png"),
          height="70%",
          width="80%")
    })
    output$embedo = renderUI({
      addResourcePath("www", "www")
      img(src = paste0(input$term, "Opium", ".png"),
          height="70%",
          width="80%")
    })
  })
  
  # Clean the main panel if user select new value
  observeEvent(input$time1,{
    output$network = renderUI(NULL)
  })
  
  observeEvent(input$topic1,{
    output$network = renderUI(NULL)
  })
  
  observeEvent(input$time2,{
    output$detail = renderUI(NULL)
  })
  
  observeEvent(input$topic2,{
    output$detail = renderUI(NULL)
  })
  
  observeEvent(input$word,{
    output$association = renderUI(NULL)
  })
  
  observeEvent(input$topic3,{
    output$association = renderUI(NULL)
  })
  
  observeEvent(input$term,{
    output$embedt = renderUI(NULL)
  })
  
  observeEvent(input$term,{
    output$embedo = renderUI(NULL)
  })
  
  
# Show figure of clusters in the modal dialog
  observeEvent(input$run3, {
    addResourcePath("www", "www")
    showModal(
      modalDialog(
      img(src = getcluster(),
          hights = "70%",
          width = "80%",
          style="text-align: center;"),
      h6("Principal Component Graph of Clusters"),
      easyClose = TRUE,
      footer = tagList(
        # Click Close to exit modal dialog
        modalButton("Close")
      )
    ))
  })
  
# show sideDoc under side bar of the documentation panel
  observeEvent(input$topic2,{
    if (input$topic2 == "Tobacco"){
      output$sidedoc = renderUI({
        addResourcePath("www", "www")
        tags$iframe(
          seamless="seamless",
          src="www/tobaccosideDoc.html",
          width = "100%",
          style="height: 100vh;"
        )
      })
    }
    if (input$topic2 == "Opium"){
      output$sidedoc = renderUI({
        addResourcePath("www", "www")
        tags$iframe(
          seamless="seamless",
          src="www/opiumSideDoc.html",
          width = "100%",
          style="height: 100vh;"
        )
      })
    }
  })
  
  
# show histograms under side bar of the network panel
  output$tobaccohist = renderUI({
    addResourcePath("www", "www")
    img(src = "www/tobaccohist.png",
        height="70%",
        width="80%")
  })
  output$opiumhist = renderUI({
    addResourcePath("www", "www")
    img(src = "www/opiumhist.png",
        height="70%",
        width="80%")
  })
}

# Run the application 
shinyApp(ui = ui, server = server)
