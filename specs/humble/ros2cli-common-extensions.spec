# Meta Package
Name:           ros-humble-ros2cli-common-extensions
Version:        0.1.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-ros2cli_common_extensions and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-ros2cli_common_extensions
Requires:       ros2-humble-ros2cli_common_extensions-devel

Obsoletes: ros-humble-ros2cli-common-extensions < 0.1.1-1

%description
Meta package for ros2cli common extensions

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.1.1-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.1.1-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.1.1-1
- Initial humble build
