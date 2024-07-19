from .endpoint import Endpoint
from flask import url_for
from cims_ui.page_helpers.google_utils import get_username, get_current_group


def get_current_selected_endpoint(endpoints, called_from):
  # Adjust multiple_entries / multiple_entries_results pages to
  # multiple_entries_original so that Header Highlights Work
  if 'multiple_entries' in called_from:
    called_from = 'multiple_entries_original'

  for endpoint in endpoints:
    if endpoint.page_name == called_from:
      endpoint.selected = True
      return endpoint.url
  return ''


def get_endpoints(called_from=None):
  # Add new endpoints here for auto-creation on all pages
  endpoints = [
      # Endpoint(
      #     'Single Search',
      #     'singlesearch',
      #     'Provide as much of the address as possible for best results.',
      #     'a_single_entry',
      # ),
      # Endpoint(
      #     'Single UPRN',
      #     'uprn',
      #     "Search for a property via its unique property reference number. This is a 12 digit number which contains no characters.",
      #     'a_single_entry',
      # ),
      # Endpoint(
      #     'Postcode',
      #     'postcode',
      #     "Search for a property using its postcode. This is effective and a valid postcode will return a list of possible addresses.",
      #     'a_single_entry',
      # ),
      # Endpoint(
      #     'Typeahead',
      #     'typeahead',
      #     "This search types ahead. Autosuggest on steroids basically. Useful if you quickly want a user to find an address.",
      #     'a_single_entry',
      # ),
      Endpoint(
          'Multiple Entries',
          'multiple_entries_original',
          "Search for not just  one address. Several. Get lots of results you can look through. This service completes many single searches from a file.",
          'b_multiple_entries',
      ),
      # Endpoint(
      #     'Multiple UPRN',
      #     'uprn_multiple_entries',
      #     "Search for multiple addresses providing mulitple UPRNs (Unique Property Reference Numbers)",
      #     'b_multiple_entries',
      # ),
      # Endpoint(
      #     'API',
      #     'custom_response',
      #     'Submit requests directly to the API and receive JSON style fromatting in return. Use this if you want to test out API features that the UI currently does not support',
      #     'd_misc_functionality',
      # ),
      # Endpoint(
      #     'Help',
      #     'help',
      #     'See information about the other pages and how to contact support.',
      #     'c_help_pages',
      #     url=url_for('help', subject='home'),
      # ),
      # Endpoint(
      #     'Settings',
      #     'settings',
      #     'User preferences are stored locally on their web-browser. Adjust or reset those settings here.',
      #     'd_misc_functionality',
      #     url=url_for('settings')),
  ]

  username = get_username()

  called_from = '' if called_from == None else called_from
  current_selected_endpoint = get_current_selected_endpoint(
      endpoints, called_from)

  # Before the nav component is made from Endpoints, remove unallowed pages

  current_group = get_current_group()
  allowed_pages = current_group.get('allowed_pages', [])

  secure_endpoints = []
  for endpoint in endpoints:
    if endpoint.page_name in allowed_pages:
      secure_endpoints.append(endpoint)

  # Create dict for ons-navigation component
  nav_info = [{
      'title': endpoint.title,
      'url': endpoint.url
  } for endpoint in secure_endpoints]

  # Add a copy of the navigation info to each Endpoint
  for endpoint in secure_endpoints:
    endpoint.nav_info = nav_info
    endpoint.current_selected_endpoint = current_selected_endpoint

  return secure_endpoints
