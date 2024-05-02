# Meta Package
Name:           ros-humble-gtest-vendor
Version:        1.10.9004
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-gtest_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-gtest_vendor
Requires:       ros2-humble-gtest_vendor-devel

Obsoletes: ros-humble-gtest-vendor < 1.10.9004-1

%description
The package provides GoogleTest.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.10.9004-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.10.9004-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.10.9004-1
- Initial humble build
