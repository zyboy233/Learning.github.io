# coding:utf-8
# __author__ = 'Gao'

import datetime
from haystack import indexes
from df_goods.models import GoodsInfo

# 这个文件的作用是设置haystack在生成索引(whoosh_index文件夹)时，根据哪些字段来生成索引(suggest)。

class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return GoodsInfo

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

