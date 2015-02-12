import sys
import os
from HTMLParser import HTMLParser

#==========================
# Constants
#==========================

root = '/var/www2/signbank/live/';
sb_video_folder = root+'writable/glossvideo/';

#==========================
# Functions
#==========================

def video_to_signbank(source_folder,gloss,extension):
        
    #Add a dot before the extension if needed
    if extension[0] != '.':
        extension = '.' + extension;

    #Figure out some names
    annotation_id = gloss.annotation_idgloss;
    pk = str(gloss.pk);
    destination_folder = sb_video_folder+annotation_id[:2]+'/';

    #Create the necessary subfolder if needed
    if not os.path.isdir(destination_folder):
        os.mkdir(destination_folder);

    #Move the file
    source = source_folder+annotation_id+extension;
    goal = destination_folder+annotation_id+'-'+pk+extension;
    os.rename(source,goal);

    return True

def unescape(string):

    return HTMLParser().unescape(string)


def compare_valuedict_to_gloss(valuedict,gloss):
    """Takes a dict of arbitrary key-value pairs, and compares them to a gloss"""

    #Create an overview of all fields, sorted by their human name
    fields = {field.verbose_name: field for field in gloss._meta.fields};

    differences = [];

    #Go through all values in the value dict, looking for differences with the gloss
    for human_key, new_human_value in valuedict.items():

        #Find the matching field in the gloss, and remember its 'real' name
        try:
            field = fields[human_key];
            machine_key = field.name;
        except KeyError:
            continue;

        #Try to translate the value to machine values if needed
        if len(field.choices) > 0:
            human_to_machine_values = {human_value: machine_value for machine_value, human_value in field.choices};

            try:
                new_machine_value = human_to_machine_values[new_human_value];
            except KeyError:
                if new_human_value == '':
                    new_human_value = 'None';
                    new_machine_value = None;

        elif field.__class__.__name__ == 'IntegerField':

            try:
                new_machine_value = int(new_human_value);
            except ValueError:
                new_human_value = 'None';
                new_machine_value = None;
        elif field.__class__.__name__ == 'NullBooleanField':

            if new_human_value in ['True','true']:
                new_machine_value = True;
            else:
                new_machine_value = False;

        else:
            if new_human_value == 'None':
                new_machine_value = None;
            else:
                new_machine_value = new_human_value

        #Try to translate the key to machine keys if possible
        try:
            original_machine_value = getattr(gloss,machine_key);
        except KeyError:
            continue;

        #Translate back the machine value from the gloss
        try:
            original_human_value = dict(field.choices)[original_machine_value]
        except KeyError:
            original_human_value = original_machine_value

        #Remove any weird char
        try:
            new_machine_value = unescape(new_machine_value)
            new_human_value = unescape(new_human_value)
        except TypeError:
            pass;

        #Check for change, and save your findings if there is one
        if original_machine_value != new_machine_value:
            differences.append({'pk':gloss.pk,
                                'idgloss':gloss.idgloss,
                                'machine_key':machine_key,
                                'human_key':human_key,
                                'original_machine_value':original_machine_value,
                                'original_human_value':original_human_value,
                                'new_machine_value':new_machine_value,
                                'new_human_value':new_human_value})

    return differences