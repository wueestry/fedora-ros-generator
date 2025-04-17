# Meta Package
Name:           ros-jazzy-gpio-controllers
Version:        4.23.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://control.ros.org
Summary:        Meta package for ros2-jazzy-gpio_controllers and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-gpio_controllers
Requires:       ros2-jazzy-gpio_controllers-devel

Obsoletes: ros-jazzy-gpio-controllers < 4.23.0-1

%description
Controllers to interact with gpios.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sun Apr 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.23.0-1
- Update to latest release
* Sat Apr 05 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.22.0-1
- Update to latest release
* Sat Mar 08 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.21.0-1
- Update to latest release
* Mon Jan 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.18.0-1
- Update to latest release
