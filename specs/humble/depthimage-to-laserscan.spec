# Meta Package
Name:           ros-humble-depthimage-to-laserscan
Version:        2.5.1
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/depthimage_to_laserscan
Summary:        Meta package for ros2-humble-depthimage_to_laserscan and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-depthimage_to_laserscan
Requires:       ros2-humble-depthimage_to_laserscan-devel

Obsoletes: ros-humble-depthimage-to-laserscan < 2.5.1-1

%description
depthimage_to_laserscan

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.5.1-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.5.1-1
- update to latest upstream release
* Tue Aug 08 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.5.1-1
- update to latest upstream
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.5.0-1
- Initial humble build
