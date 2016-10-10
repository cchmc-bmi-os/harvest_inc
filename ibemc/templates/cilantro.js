var csrf_token = '{{ csrf_token }}',

    require = {
        baseUrl: '{{ STATIC_URL }}cilantro/js',
        paths: {
            'project': '{{ JAVASCRIPT_URL }}'
        }
    },

    cilantro = {
        url: '{% url "serrano:root" %}',
        root: '{{ request.META.SCRIPT_NAME }}',
        main: '#content',
        statsModelsList: [],
        threshold: 10000,
        fields: {
            defaults: {
                stats: false,
                form: {
                    controls: ['infoBars']
                }
            },
            instances: {
            // Ibemc Id
            313: {
                form: {
                    controls: ['search']
                }
            }
        }

        },
    };
