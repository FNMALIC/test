/**
 * @file
 * JavaScript behaviors for Telephone element.
 */

(function ($, Drupal, drupalSettings) {

  'use strict';

  // @see https://github.com/jackocnr/intl-tel-input#options
  Drupal.hubber_customers = Drupal.hubber_customers || {};
  Drupal.hubber_customers.intlTelInput = Drupal.hubber_customers.intlTelInput || {};

  /**
   * Initialize Telephone international element.
   * @see http://intl-tel-input.com/node_modules/intl-tel-input/examples/gen/is-valid-number.html
   * @type {Drupal~behavior}
   */
  Drupal.behaviors.hubberCustomersTelephoneInternational = {
    attach: function (context, settings) {
      if (!$.fn.intlTelInput) {
        return;
      }

      var reset_js_invalid = function (element) {
        if (element.hasClass('js-invalid')) {
          element.removeClass('js-invalid');
        }
      };

      var destroy_input_tel = function (element, field_name) {
        if (element.closest('.iti.iti--allow-dropdown').next().hasClass(field_name)) {
          element.closest('.iti.iti--allow-dropdown').next('.' + field_name).remove();
        }
      };

      $(context).find('input[name="field_user_phone[0][value]').once('hubber-customer-changevalue-user-phone').on('blur', function() {
        reset_js_invalid($(this));
        destroy_input_tel($(this), 'error-user-phone');
      });

      $(context).find('input[name="field_user_mobile[0][value]').once('hubber-customer-changevalue-user-mobile').on('blur', function() {
        reset_js_invalid($(this));
        destroy_input_tel($(this), 'error-user-mobile');
      });

      $(context).find('.js-form-submit').once('hubber-customer-js-form-submit').click(function() {

        if (settings.invalidField !== undefined) {
          settings.invalidField = undefined;
        }

        var $field_user_phone = $('input[name="field_user_phone[0][value]"]');
        var $field_user_mobile = $('input[name="field_user_mobile[0][value]"]');
        var $field_tel = $('input[type="tel"]');
        var $error_user_mobile =  $('.error-user-phone');

        destroy_input_tel($field_user_phone, 'error-user-phone');
        destroy_input_tel($field_user_mobile, 'error-user-mobile');

        if ($error_user_mobile.length > 0) {
          $error_user_mobile.remove();
        }

        var $required_mobile = $field_user_mobile.attr('required');
        var $required_phone = $field_user_phone.attr('required');
        var $required_field_tel = $field_tel.attr('required');

        if ($required_mobile === 'required') {
          if ($field_user_mobile.length > 0 && $field_user_mobile.val() === '+33') {
            $field_user_mobile.addClass('js-invalid');
            $field_user_mobile.closest('.iti.iti--allow-dropdown').after('<div class="error-user-mobile form-item--error-message">' + Drupal.t('Please fill in this field.') + '</div>');
          }
        }

        if ($required_phone === 'required') {
          if ($field_user_phone.length > 0 && $field_user_phone.val() === '+33') {
            $field_user_phone.addClass('js-invalid');
            $field_user_phone.closest('.iti.iti--allow-dropdown').after('<div class="error-user-phone form-item--error-message">' + Drupal.t('Please fill in this field.') + '</div>');
          }
        }

        if ($required_field_tel === 'required') {
          if ($field_tel.length > 0 && $field_tel.val() === '+33' && ($field_user_phone.length === 0 || $field_user_mobile.length === 0) ) {
            $field_tel.addClass('js-invalid');
            $field_tel.closest('.iti.iti--allow-dropdown').after('<div class="error-user-phone form-item--error-message">' + Drupal.t('Please fill in this field.') + '</div>');
          }
        }

      });

      $(context).find('input.intl-telephone').once('hubber-customers-telephone-international').each(function () {
        var $telephone = $(this);

        // Add error message container.
        var $error = $('<div class="form-item--error-message">' + Drupal.t('Invalid phone number') + '</div>').hide();
        $telephone.closest('.js-form-item').append($error);

        var options = {
          utilsScript: drupalSettings.hubber_customers.intlTelInput.utilsScript,
          nationalMode: false,
          initialCountry: 'FR',
          preferredCountries: ['FR']
        };
        $telephone.intlTelInput(options);

        var reset = function () {
          // Mark the field as valid
          $telephone[0].setCustomValidity('');

          $telephone.removeClass('error js-invalid');
          $telephone.closest('.js-form-item');
          $error.hide();
        };

        $telephone.on('blur', function () {
          reset();
        });

        $telephone.on('keyup change', reset);
      });
    }
  };

})(jQuery, Drupal, drupalSettings);
;
/**
 * @file
 * JavaScript behaviors for options elements.
 */

(function ($, Drupal) {

  'use strict';

  /**
   * Attach handlers to options buttons element.
   *
   * @type {Drupal~behavior}
   */
  Drupal.behaviors.webformOptionsButtons = {
    attach: function (context) {
      // Place <input> inside of <label> before the label.
      $(context).find('label.webform-options-display-buttons-label > input[type="checkbox"], label.webform-options-display-buttons-label > input[type="radio"]').each(function () {
        var $input = $(this);
        var $label = $input.parent();
        $input.detach().insertBefore($label);
      });
    }
  };

})(jQuery, Drupal);
;
/**
 * @file
 * Defines Javascript behaviors for the commerce cart module.
 */

(function ($, Drupal, drupalSettings) {
  'use strict';

  Drupal.behaviors.commerceCartBlock = {
    attach(context) {
      const $context = $(context);
      const $cart = $context.find('.cart--cart-block').addBack('.cart--cart-block');
      const $cartContents = $cart.find('.cart-block--contents');

      if ($cartContents.length > 0) {
        // Expand the block when the link is clicked.
        $(once('cart-button-processed', '.cart-block--link__expand', context)).on('click', (e) => {
          // Prevent it from going to the cart.
          e.preventDefault();
          // Get the shopping cart width + the offset to the left.
          const windowWidth = $(window).width();
          const cartWidth = $cartContents.width() + $cart.offset().left;
          // If the cart goes out of the viewport we should align it right.
          if (cartWidth > windowWidth) {
            $cartContents.addClass('is-outside-horizontal');
          }
          // Toggle the expanded class.
          $cartContents
            .toggleClass('cart-block--contents__expanded')
            .slideToggle();
        });
      }
    }
  };
})(jQuery, Drupal, drupalSettings);
;
/**
* DO NOT EDIT THIS FILE.
* See the following change record for more information,
* https://www.drupal.org/node/2815083
* @preserve
**/

(function (Drupal, drupalSettings) {
  function mapTextContentToAjaxResponse(content) {
    if (content === '') {
      return false;
    }

    try {
      return JSON.parse(content);
    } catch (e) {
      return false;
    }
  }

  function bigPipeProcessPlaceholderReplacement(placeholderReplacement) {
    var placeholderId = placeholderReplacement.getAttribute('data-big-pipe-replacement-for-placeholder-with-id');
    var content = placeholderReplacement.textContent.trim();

    if (typeof drupalSettings.bigPipePlaceholderIds[placeholderId] !== 'undefined') {
      var response = mapTextContentToAjaxResponse(content);

      if (response === false) {
        once.remove('big-pipe', placeholderReplacement);
      } else {
        var ajaxObject = Drupal.ajax({
          url: '',
          base: false,
          element: false,
          progress: false
        });
        ajaxObject.success(response, 'success');
      }
    }
  }

  var interval = drupalSettings.bigPipeInterval || 50;
  var timeoutID;

  function bigPipeProcessDocument(context) {
    if (!context.querySelector('script[data-big-pipe-event="start"]')) {
      return false;
    }

    once('big-pipe', 'script[data-big-pipe-replacement-for-placeholder-with-id]', context).forEach(bigPipeProcessPlaceholderReplacement);

    if (context.querySelector('script[data-big-pipe-event="stop"]')) {
      if (timeoutID) {
        clearTimeout(timeoutID);
      }

      return true;
    }

    return false;
  }

  function bigPipeProcess() {
    timeoutID = setTimeout(function () {
      if (!bigPipeProcessDocument(document)) {
        bigPipeProcess();
      }
    }, interval);
  }

  bigPipeProcess();
  window.addEventListener('load', function () {
    if (timeoutID) {
      clearTimeout(timeoutID);
    }

    bigPipeProcessDocument(document);
  });
})(Drupal, drupalSettings);;
