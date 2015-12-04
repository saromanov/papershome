from django.utils import timezone
from home.models import Paper

p = Paper(title='Segmental Recurrent Neural Networks',
description='We introduce segmental recurrent neural networks(SRNNs) which define, given an input sequence, a joint probability distribution over segmentations of the input and labelings of the segments. Representations of the input segments(i.e., contiguous subsequences of the input) are computed by encoding their constituent tokens using bidirectional recurrent neural nets, and these "segment embeddings" are used to define compatibility scores with output labels. These local compatibility scores are integrated using a global semi - Markov conditional random field. Both fully supervised training - - in which segment boundaries and labels are observed - - as well as partially supervised training - - in which segment boundaries are latent - - are straightforward. Experiments on handwriting recognition and joint Chinese word segmentation / POS tagging show that, compared to models that do not explicitly represent segments such as BIO tagging schemes and connectionist temporal classification(CTC), SRNNs obtain substantially higher accuracies.', pubdate=timezone.now(),
author='Lingpeng Kong, Chris Dyer, Noah A. Smith', version='1', link='http: // arxiv.org / abs / 1511.06018')
p.tags.add('RNN', 'BRNN')
p.save()
