import cloudblaze.blazeweb.models as models
import cloudblaze.continuumweb.bbmodel as bbmodel

def new_doc(flaskapp, docid, title, rw_users=None, r_users=None):
    plot_context = bbmodel.ContinuumModel(
        'CDXPlotContext', docs=[docid])
    flaskapp.collections.add(plot_context)
    if rw_users is None: rw_users = []
    if r_users is None: r_users = []
    doc = Doc(docid, title, rw_users, r_users, plot_context.ref())
    doc.save(flaskapp.model_redis)
    return doc

class Doc(models.ServerModel):
    typename = 'doc'
    idfield = 'docid'
    
    def __init__(self, docid, title, rw_users, r_users, plot_context_ref):
        self.docid = docid
        self.title = title
        self.rw_users = rw_users
        self.r_users = r_users
        self.plot_context_ref = plot_context_ref
        
    def to_json(self):
        return {'docid' : self.docid,
                'title' : self.title,
                'rw_users' : self.rw_users,
                'r_users' : self.r_users,
                'plot_context_ref' : self.plot_context_ref}
    
    @staticmethod
    def from_json(obj):
        return Doc(obj['docid'], obj['title'],
                   obj['r_users'], obj['rw_users'],
                   obj['plot_context_ref'])
    

