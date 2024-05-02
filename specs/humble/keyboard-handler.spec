# Meta Package
Name:           ros-humble-keyboard-handler
Version:        0.0.5
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-keyboard_handler and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-keyboard_handler
Requires:       ros2-humble-keyboard_handler-devel

Obsoletes: ros-humble-keyboard-handler < 0.0.5-1

%description
Handler for input from keyboard

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.0.5-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.0.5-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.0.5-1
- Initial humble build
