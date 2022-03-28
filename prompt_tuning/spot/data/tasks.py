# Copyright 2022 Google.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Import tasks."""

# pylint: disable=unused-import,g-import-not-at-top
from prompt_tuning.spot.data import gem
from prompt_tuning.spot.data import glue
from prompt_tuning.spot.data import mrqa
from prompt_tuning.spot.data import nli
from prompt_tuning.spot.data import rainbow
from prompt_tuning.spot.data import sentiment
from prompt_tuning.spot.data import similarity
from prompt_tuning.spot.data import summarization
from t5.data import tasks as t5_tasks
