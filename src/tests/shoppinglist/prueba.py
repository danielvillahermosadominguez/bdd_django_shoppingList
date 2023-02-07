from abc import abstractmethod


class SlidePresenter:
  
    def __init__(self, datos, slide):
        self.datos = datos
        self.slide = slide
    
    def process_slide(self):
        pass

class SlidePresenterLiquity(SlidePresenter):
    
    def __init__(self, datos):
        self.datos = datos

    def process_slide(self, slide):
        super.__init__(self, slide):
        self.datos = datos
        print("movidas acopladas al")


class SlideLoader:
      def __init__(self, file, slide_presenters):
          self.file = file
          self.dict =slide_presenters

      
       def generate():
            prs = Presentation(file)

            for idx, slide in enumerate(prs.slides):
                slide_presenter = dict[idx] 
                slide_presenter.process_slide(slide)
                

        prs.save(file)

