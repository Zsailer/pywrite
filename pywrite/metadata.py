import pickle

class Data(object):
    
    def __init__(self):
        pass

class Metadata(object):
    
    def __init__(self, **kwargs):
        self.add_data(**kwargs)
            
    def save(self, fname):
        """ Write to a pickle file. """
        f = open(fname, "wb")
        pickle.dump(self, f)
        f.close()
        
    def add_data(self, **kwargs):
        # Iterate through kwargs
        for k in kwargs:
            setattr(self, k, kwargs[k])
            
    @classmethod
    def write(cls, fname, **kwargs):
        data = cls(**kwargs) 
        data.save(fname)