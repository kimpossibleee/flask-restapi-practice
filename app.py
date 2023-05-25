from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

cats = []

class CatNames(Resource):
    def get(self,name):
        for cat in cats:
            if cat['name'] == name:
                return cat
        return {'name':None},404

    def post(self, name):
        cat = {'name':name}
        cats.append(cat)
        print(cats)
        return cat

    def delete(self,name):
        for index,cat in enumerate(cats):
            if cat['name'] == name:
                deleted_cat = cats.pop(index)
                return {f'You have deleted {deleted_cat} :)'}

class AllNames(Resource):
    def get(self):
        return cats

api.add_resource(CatNames, '/cat/<string:name>')
api.add_resource(AllNames,'/cats')

if __name__ == '__main__':
    app.run(debug=True)
