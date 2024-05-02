# Meta Package
Name:           ros-humble-rqt-shell
Version:        1.0.2
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/rqt_shell
Summary:        Meta package for ros2-humble-rqt_shell and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-rqt_shell
Requires:       ros2-humble-rqt_shell-devel

Obsoletes: ros-humble-rqt-shell < 1.0.2-1

%description
rqt_shell is a Python GUI plugin providing an interactive shell.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.2-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.2-1
- update to latest upstream release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.2-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.0.4.11-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.2-1
- Initial humble build
