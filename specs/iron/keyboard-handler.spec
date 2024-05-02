# Meta Package
Name:           ros-iron-keyboard-handler
Version:        0.1.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-keyboard_handler and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-keyboard_handler
Requires:       ros2-iron-keyboard_handler-devel

Obsoletes: ros-iron-keyboard-handler < 0.1.0-1

%description
Handler for input from keyboard

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.1.0-1
- Update to latest release
