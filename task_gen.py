import g
import data

def gen():
    power_set = f'''
        <?cml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE topic PUBLIC "-//OASIS//DTD DITA Topic//EN" "topic.dtd">
        <task id="power_set">
            <title>Come Impostare la Produzione di Ozono</title>
            <taskbody>
                <context>
                    <image href="projects/aurora/resources/images/demo_p_home_off.png" alt=""/>
                    <image href="projects/aurora/resources/images/demo_generators_p_home_set.png" alt=""/>
                    <image href="projects/aurora/resources/images/demo_p_password.png" alt=""/>
                    <image href="projects/aurora/resources/images/demo_generators_p_set_power.png" alt=""/>
                    <image href="projects/aurora/resources/images/demo_p_generators_select.png" alt=""/>
                    <image href="projects/aurora/resources/images/demo_p_generators_save.png" alt=""/>
                    <image href="projects/aurora/resources/images/demo_p_set_back.png" alt=""/>
                    <image href="projects/aurora/resources/images/demo_p_home_generators.png" alt=""/>
                    <image href="projects/aurora/resources/images/demo_p_home_power_on.png" alt=""/>
                </context>
                <steps>
                    <step>
                        <cmd>{data.DISPLAY_PAGE_HOME_POWER_OFF}</cmd>
                    </step>
                    <step>
                        <cmd>{data.DISPLAY_PAGE_HOME_SETTINGS}</cmd>
                    </step>
                    <step>
                        <cmd>{data.DISPLAY_PAGE_PASSWORD}</cmd>
                    </step>
                    <step>
                        <cmd>{data.DISPLAY_PAGE_SETTINGS_GENERATORS}</cmd>
                    </step>
                    <step>
                        <cmd>{data.DISPLAY_PAGE_GENERATORS_ARROWS}</cmd>
                    </step>
                    <step>
                        <cmd>{data.DISPLAY_ICON_SAVE}</cmd>
                    </step>
                    <step>
                        <cmd>{data.DISPLAY_PAGE_SETTINGS_BACK}</cmd>
                    </step>
                    <step>
                        <cmd>{data.DISPLAY_PAGE_HOME_GENERATORS}</cmd>
                    </step>
                    <step>
                        <cmd>{data.DISPLAY_PAGE_HOME_POWER_ON}</cmd>
                    </step>
                </steps>
                <result>
                    <p>The generator now produces ozone only during the times set in the calendar.</p>
                </result>
            </taskbody>
        </task>
    '''.strip()
    with open(f'{g.TASKS_FOLDERPATH}/power_set.dita', 'w') as f: f.write(power_set)

    calendar_enable = f'''
        <?cml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE topic PUBLIC "-//OASIS//DTD DITA Topic//EN" "topic.dtd">
        <task id="calendar-enable">
            <title>Come Abilitare il Calendario</title>
            <taskbody>
                <context>
                    <image href="projects/aurora/resources/images/demo_p_home_off.png" alt=""/>
                    <image href="projects/aurora/resources/images/demo_generators_p_home_set.png" alt=""/>
                    <image href="projects/aurora/resources/images/demo_p_password.png" alt=""/>
                    <image href="projects/aurora/resources/images/demo_p_set_cal.png" alt=""/>
                    <image href="projects/aurora/resources/images/demo_p_cal_on.png" alt=""/>
                    <image href="projects/aurora/resources/images/demo_p_cal_on_save.png" alt=""/>
                    <image href="projects/aurora/resources/images/demo_p_set_back.png" alt=""/>
                    <image href="projects/aurora/resources/images/demo_p_home_cal_on.png" alt=""/>
                    <image href="projects/aurora/resources/images/demo_p_home_cal_on_power_on.png" alt=""/>
                </context>
                <steps>
                    <step>
                        <cmd>{data.DISPLAY_PAGE_HOME_POWER_OFF}</cmd>
                    </step>
                    <step>
                        <cmd>{data.DISPLAY_PAGE_HOME_SETTINGS}</cmd>
                    </step>
                    <step>
                        <cmd>{data.DISPLAY_PAGE_PASSWORD}</cmd>
                    </step>
                    <step>
                        <cmd>{data.DISPLAY_PAGE_SETTINGS_CALENDAR_ENABLE}</cmd>
                    </step>
                    <step>
                        <cmd>{data.DISPLAY_PAGE_CALENDAR_ENABLE_ON}</cmd>
                    </step>
                    <step>
                        <cmd>{data.DISPLAY_PAGE_CALENDAR_ENABLE_SAVE}</cmd>
                    </step>
                    <step>
                        <cmd>{data.DISPLAY_PAGE_SETTINGS_BACK}</cmd>
                    </step>
                    <step>
                        <cmd>{data.DISPLAY_PAGE_HOME_CALENDAR_ENABLE}</cmd>
                    </step>
                    <step>
                        <cmd>{data.DISPLAY_PAGE_HOME_POWER_ON}</cmd>
                    </step>
                </steps>
                <result>
                    <p>The generator now produces ozone only during the times set in the calendar.</p>
                </result>
            </taskbody>
        </task>
    '''.strip()
    with open(f'{g.TASKS_FOLDERPATH}/calendar-enable.dita', 'w') as f: f.write(calendar_enable)

    calendar_disable = f'''
        <?cml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE topic PUBLIC "-//OASIS//DTD DITA Topic//EN" "topic.dtd">
        <task id="calendar-disable">
            <title>Come Disabilitare il Calendario</title>
            <taskbody>
                <context>
                    <image href="projects/aurora/resources/images/demo_p_home_off.png" alt=""/>
                    <image href="projects/aurora/resources/images/demo_generators_p_home_set.png" alt=""/>
                    <image href="projects/aurora/resources/images/demo_p_password.png" alt=""/>
                    <image href="projects/aurora/resources/images/demo_p_set_cal.png" alt=""/>
                    <image href="projects/aurora/resources/images/demo_p_cal_off.png" alt=""/>
                    <image href="projects/aurora/resources/images/demo_p_cal_off_save.png" alt=""/>
                    <image href="projects/aurora/resources/images/demo_p_set_back.png" alt=""/>
                    <image href="projects/aurora/resources/images/demo_p_home_cal_off.png" alt=""/>
                    <image href="projects/aurora/resources/images/demo_p_home_cal_off_power_on.png" alt=""/>
                </context>
                <steps>
                    <step>
                        <cmd>{data.DISPLAY_PAGE_HOME_POWER_OFF}</cmd>
                    </step>
                    <step>
                        <cmd>{data.DISPLAY_PAGE_HOME_SETTINGS}</cmd>
                    </step>
                    <step>
                        <cmd>{data.DISPLAY_PAGE_PASSWORD}</cmd>
                    </step>
                    <step>
                        <cmd>{data.DISPLAY_PAGE_SETTINGS_CALENDAR_ENABLE}</cmd>
                    </step>
                    <step>
                        <cmd>{data.DISPLAY_PAGE_CALENDAR_ENABLE_OFF}</cmd>
                    </step>
                    <step>
                        <cmd>{data.DISPLAY_PAGE_CALENDAR_ENABLE_SAVE}</cmd>
                    </step>
                    <step>
                        <cmd>{data.DISPLAY_PAGE_SETTINGS_BACK}</cmd>
                    </step>
                    <step>
                        <cmd>{data.DISPLAY_PAGE_HOME_CALENDAR_DISABLE}</cmd>
                    </step>
                    <step>
                        <cmd>{data.DISPLAY_PAGE_HOME_POWER_ON}</cmd>
                    </step>
                </steps>
                <result>
                    <p>The generator now produces ozone only during the times set in the calendar.</p>
                </result>
            </taskbody>
        </task>
    '''.strip()

    with open(f'{g.TASKS_FOLDERPATH}/calendar-disable.dita', 'w') as f: f.write(calendar_disable)

gen()
